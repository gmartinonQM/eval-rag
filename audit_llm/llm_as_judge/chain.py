import os
from datetime import datetime
from typing import Any, Union

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import AzureChatOpenAI
from pydantic import SecretStr

from audit_llm.llm_as_judge.prompt import (
    Prompt,
)
from audit_llm.utils.backoff import backoff
from audit_llm.utils.langfuse_utils import LangfuseUtils

load_dotenv()


class Chain:
    def __init__(
        self,
        metric: str,
        model_name: str = "gpt-4o",
        temperature: int = 0,
    ):
        deployment_name = (
            os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME_MINI")
            if model_name == "gpt-4o-mini"
            else os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME_FULL")
        )

        self.model_name = model_name
        self.temperature = temperature

        prompt = Prompt(metric)
        self.prompt = prompt.get_langchain_prompt(
            self.model_name, self.temperature
        )
        current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.session_id = (
            f"{metric}_{model_name}_v{prompt.current_version}"
            f"_{current_date}"
        )

        self.langfuse_callback_handler = LangfuseUtils.create_callback_handler(
            session_id=self.session_id
        )

        self.model = AzureChatOpenAI(
            api_key=SecretStr(os.getenv("AZURE_OPENAI_API_KEY") or ""),
            azure_endpoint=deployment_name,
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            temperature=self.temperature,
            model=model_name,
            callbacks=[self.langfuse_callback_handler],
        )
        self.parser = JsonOutputParser()

        self.chain = self.prompt | self.model | self.parser

    @backoff(retries=5)
    def get_model_response(
        self,
        inputs: Union[dict[Any, Any], list[dict[Any, Any]]],
        batch: bool = False,
    ) -> Union[Any, list[Any]]:
        """
        Processes input data and retrieves a model response.

        Parameters
        ----------
        inputs : Union[llmJudgeInput, list[llmJudgeInput]]
            The input(s) to be processed by the model. Can be a single input or
            a list of inputs.
        batch : bool, optional
            If True, processes the inputs in batch mode. Defaults to False.

        returns
        -------
        Union[Any,list[Any]]
            The model's response(s). If an error occurs, the
            response will include a dictionary with an "error" key containing
            the error message and a "response" key with the raw response
            content.

        Raises
        ------
        Exception
            If an error occurs during the invocation of the model chain, it is
            caught and logged, and the error details are included in the
            returned response.
        """
        try:
            if batch:
                response = self.chain.batch(
                    inputs if isinstance(inputs, list) else [inputs]
                )
                return response
            else:
                if isinstance(inputs, dict):
                    response = self.chain.invoke(inputs)
                else:
                    raise TypeError(
                        "Expected 'inputs' to be a dictionary when 'batch' is"
                        " False."
                    )
                return response

        except Exception as e:
            raise e  # Re-raise the exception for further handling
