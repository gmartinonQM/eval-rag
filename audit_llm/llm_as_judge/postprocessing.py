import os
from typing import Any, Callable, Tuple

import pandas as pd

from audit_llm.llm_as_judge.chain import Chain
from audit_llm.utils.file_handler import save_json
from audit_llm.utils.langfuse_utils import LangfuseUtils


def postprocess_output_llm_as_judge(
    df_output_llm: pd.DataFrame,
    metric: str,
) -> pd.DataFrame:
    """
    Processes LLM output by normalizing and renaming columns.

    Parameters
    ----------
    df_output_llm : pd.DataFrame
        DataFrame containing LLM output with a column
        'predict_llm_judge_metric'.
    metric : str
        The metric used for processing, e.g., "deductibility".

    Returns
    -------
    pd.DataFrame
        Processed DataFrame with normalized and renamed columns.
    """
    df_output_llm = df_output_llm.join(
        pd.json_normalize(df_output_llm["predict_llm_judge_metric"])
    )
    df_output_llm.rename(
        columns={
            "label": f"{metric}_label",
            "raison": f"{metric}_raison",
        },
        inplace=True,
    )
    return df_output_llm


def save_postprocessed_data(
    augmented_data: pd.DataFrame,
    func: Callable[[pd.DataFrame, str], pd.DataFrame],
    metric: str,
    root_abspath: str,
    current_date: str,
) -> None:
    """
    Postprocesses augmented data and saves it as a JSON file.
    Parameters
    ----------
    augmented_data : pd.DataFrame
        DataFrame containing LLM predictions.
    func : Callable
        Function to postprocess the DataFrame.
    metric : str
        Name of the metric.
    root_abspath : str
        Root directory for output.
    current_date : str
        Date string for the output filename.
    Returns
    -------
    None
    """
    postprocessed_data = func(augmented_data, metric)

    output_filename = f"{metric}_dataframes_{current_date}.json"
    file_path = os.path.abspath(f"{root_abspath}/output/{output_filename}")

    postprocessed_data.to_json(file_path)


def save_metric_results(
    augmented_data: pd.DataFrame,
    func: Callable[[pd.DataFrame], Tuple[dict[str, Any], float]],
    metric: str,
    model: Chain,
    root_abspath: str,
    current_date: str,
    model_name: str,
    temperature: int,
) -> None:
    """
    Computes metric results, saves them to a JSON file and
    sends them to Langfuse.

    Parameters
    ----------
    augmented_data : pd.DataFrame
        DataFrame containing augmented data with LLM predictions.
    metric : str
        The metric used for processing, e.g., "deductibility".
    model : Chain
        The chain instance.
    root_abspath : str
        Root absolute path for saving the output files.
    current_date : str
        Current date string for naming the output files.
    model_name : str
        Name of the model used.
    temperature : int
        Temperature setting for the model.
    """
    output_filename = f"{metric}_results_{current_date}.json"
    file_path = os.path.abspath(f"{root_abspath}/output/{output_filename}")

    results, metric_ratio = func(augmented_data)
    save_json(file_path, results)

    LangfuseUtils.save_trace_langfuse(
        data=results,
        trace_name=f"General_{metric}_{current_date}",
        model_name=model_name,
        parameters={"temperature": temperature},
        prompt=model.prompt.template,
        scores={f"{metric}": metric_ratio},
        session_id=model.session_id,
    )
