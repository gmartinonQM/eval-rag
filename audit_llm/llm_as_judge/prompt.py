import importlib
from typing import Union

from langchain.prompts import PromptTemplate
from langfuse.api.resources.commons.errors.not_found_error import NotFoundError
from langfuse.model import TextPromptClient

from audit_llm.utils.langfuse_utils import LangfuseUtils


class Prompt:
    def __init__(self, metric: str) -> None:
        utils = LangfuseUtils()
        self._langfuse = utils.get_session()
        self.langfuse_prompt: TextPromptClient = None

        if metric == "faithfulness":
            self.metric = metric
            self.module = importlib.import_module(
                "audit_llm.faithfulness.prompts_template"
                f".prompt_template_{self.metric}"
            )

        if metric == "speculation":
            self.metric = metric
            self.module = importlib.import_module(
                "audit_llm.faithfulness.prompts_template"
                f".prompt_template_{self.metric}"
            )

        if metric == "relevancy":
            self.metric = metric
            self.module = importlib.import_module(
                f"audit_llm.{self.metric}.prompts_template.prompt_template"
            )

        self.current_version = self.module.CURRENT_VERSION
        self.prompt_template = self.module.prompt_template

    def get_langfuse_prompt(
        self, version: int, label: str
    ) -> Union[TextPromptClient, None]:
        """
        Retrieve a Langfuse prompt based on the specified version and label.

        Parameters
        ----------
        version : int
            The version number of the prompt to retrieve.
        label : str
            The label associated with the prompt.

        Returns
        -------
        Union[TextPromptClient, None]
            The retrieved prompt object if found, otherwise None.

        Raises
        ------
        NotFoundError
            If the specified prompt is not found.
        BaseException
            For any unexpected errors encountered during retrieval.
        """
        try:
            return self._langfuse.get_prompt(
                name=f"{self.metric}-checker-v{version}", label=label
            )
        except NotFoundError:  # Explicitly catch the NotFoundError
            print(
                f"Prompt not found: {self.metric}-checker-v{version} with label"
                f" '{label}'"
            )
            return None
        except BaseException as e:
            print(f"Unexpected error while fetching prompt: {e}")
            return None

    def set_langfuse_prompt(self, langfuse_prompt: TextPromptClient) -> None:
        """
        Set the Langfuse prompt client for the instance.

        Parameters
        ----------
        langfuse_prompt : TextPromptClient
            The Langfuse prompt client to be set for the instance.

        Returns
        -------
        None
        """
        self.langfuse_prompt = langfuse_prompt

    def get_langchain_prompt(
        self, model_name: str, temperature: int
    ) -> PromptTemplate:
        """
        Generate a LangChain prompt template for evaluating metric of
        statements.

        This method creates a prompt template designed to assess the
        deductibility of information in given statements based on provided
        reference sources.
        It uses Langfuse to manage and version the prompt, ensuring consistency
        and traceability.

        Parameters
        ----------
        model_name : str
            The name of the model to be used for the prompt.
        temperature : int
            The temperature setting for the model, controlling output
            randomness.

        Returns
        -------
        PromptTemplate
            A LangChain PromptTemplate object configured with the generated
            prompt.

        Notes
        -----
        - The prompt instructs the model to classify statements as either
          assertive (deductible or non-deductible) or non-assertive.
        - The output format is strictly defined as a JSON structure.
        - Example inputs, statements, and outputs are embedded in the prompt
          for clarity.
        """

        if not self.langfuse_prompt:
            self._langfuse.create_prompt(
                name=f"{self.metric}-checker-v{self.current_version}",
                prompt=self.prompt_template,
                config={
                    "model": model_name,
                    "temperature": temperature,
                    "version": self.current_version,
                },
                labels=["test"],
            )
            self.set_langfuse_prompt(
                self._langfuse.get_prompt(
                    name=f"{self.metric}-checker-v{self.current_version}",
                    label="test",
                )
            )

        prompt = PromptTemplate.from_template(
            self.langfuse_prompt.get_langchain_prompt(),
            metadata={"langfuse_prompt": self.langfuse_prompt},
        )

        return prompt

    def get_prompt(self) -> PromptTemplate:
        """
        Generates a PromptTemplate instance from the stored prompt template.
        Returns
        -------
        PromptTemplate
            An instance of PromptTemplate created from the object's
            prompt_template attribute.
        """

        prompt = PromptTemplate.from_template(self.prompt_template)

        return prompt
