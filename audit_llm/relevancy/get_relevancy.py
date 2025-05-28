import datetime
import glob
import os
from typing import Any, Tuple

import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm

from audit_llm.llm_as_judge.chain import Chain
from audit_llm.llm_as_judge.metrics import get_metric_rate
from audit_llm.llm_as_judge.postprocessing import (
    postprocess_output_llm_as_judge,
    save_metric_results,
    save_postprocessed_data,
)
from audit_llm.relevancy.dataclass import llmJudgeInput
from audit_llm.utils.batch_utils import get_batch_indices

load_dotenv()


def run_llm_as_judge(
    source_data: pd.DataFrame,
    metric: str,
    batch_size: int,
    model_name: str = "gpt-4o",
    temperature: int = 0,
) -> Tuple[pd.DataFrame, Chain]:
    """
    Processes data to compute metric scores for grouped sentences.

    Parameters
    ----------
    source_data : pd.DataFrame
        DataFrame containing grouped sentence data.
    metric : str
        The metric to be used for processing, e.g., "metric".
    batch_size : int
        Number of rows to process per chunk.
    model_name : str, optional
        Name of the model to use, by default "gpt-4o".
    temperature : int, optional
        Temperature setting for the model, by default 0.

    Returns
    -------
    Tuple[pd.DataFrame, Model]
        Updated DataFrame with predictions and the model instance.

    Examples
    --------
    Process data starting from the first chunk:
    >>> run_llm_as_judge(source_data, batch_size=100)
    Process data starting from a specific chunk:
    >>> run_llm_as_judge(source_data, batch_size=100, _start_batch=3)
    """
    model = Chain(metric, model_name=model_name, temperature=temperature)

    n_rows = source_data.shape[0]
    start_index_batch = 0
    num_batch = n_rows // batch_size + 1 if batch_size > 0 else 1
    index_left = source_data.index

    if "predict_llm_judge_metric" in source_data.columns:
        source_data_na = source_data[
            source_data["predict_llm_judge_metric"].isna()
        ].copy()

        index_left = source_data_na.index
        n_index_left = index_left.shape[0]
        num_batch = n_index_left // batch_size + 1 if batch_size > 0 else 1

    for batch_index in tqdm(
        range(start_index_batch, num_batch), desc="Processing Batches"
    ):
        start_index, end_index = get_batch_indices(
            batch_size, batch_index, n_rows
        )

        index_to_compute = index_left[start_index:end_index]
        end_index = min(end_index, index_left.shape[0])

        if end_index < batch_size:
            index_to_compute = index_left[start_index:]

        print(
            "\nbatch index : start_index, end_index",
            start_index,
            end_index,
        )
        print("df index : ", index_to_compute)

        data_batch_as_dict = source_data.loc[index_to_compute].to_dict(
            orient="records"
        )

        input = [
            llmJudgeInput(
                question_fr=data["questions - fr"],
                answer=data["answer"],
            ).model_dump()
            for data in data_batch_as_dict
        ]

        try:
            predict_llm_judge_metric = model.get_model_response(
                input,
                batch=True,
            )

            source_data.loc[
                index_to_compute,
                "predict_llm_judge_metric",
            ] = predict_llm_judge_metric

        except Exception as e:
            print(
                f"Error processing batch {batch_index} with start index "
                f"{start_index} and end index {end_index}:\n"
                f"Original error: {e}"
            )

        assert "predict_llm_judge_metric" in source_data.columns

        source_data.to_pickle(f"tmp/tmp_{metric}.pkl")

    return source_data, model


def compute_metric_score(
    output_llm_judge: pd.DataFrame,
) -> Tuple[dict[str, Any], float]:
    """
    Computes metric scores from a DataFrame of LLM judge outputs.
    Parameters
    ----------
    output_llm_judge : pd.DataFrame
        DataFrame containing LLM judge outputs with required columns:
        'questions - fr', 'answer', and 'predict_llm_judge_metric'
        (dict with 'raison' and 'label').

    Returns
    -------
    results : dict of str, Any
        Dictionary mapping row indices to extracted question, answer, reason,
        and binary label.

    metric_ratio : float
        Ratio of positive metric labels over total rows.

    Raises
    ------
    ValueError
        If a row cannot be processed due to missing or malformed data.
    """

    results = {}
    for index, row in output_llm_judge.iterrows():
        try:
            results[index] = {
                "Question": row["questions - fr"],
                "answers": row["answer"],
                "raison": row["predict_llm_judge_metric"]["raison"],
                "label": 1
                if row["predict_llm_judge_metric"]["label"] == "1"
                else 0,
            }
        except Exception as e:
            raise ValueError(
                f"Error processing row at index {index}:\nRow content: {row}"
                f"\nOriginal error: {e}"
            ) from e

    n_rows = output_llm_judge.shape[0]
    metric_ratio = get_metric_rate(results, n_rows)

    return results, metric_ratio


if __name__ == "__main__":
    batch_size = int(os.getenv("batch_size", 100))
    model_name = os.getenv("MODEL_NAME", "gpt-4o")
    temperature = int(os.getenv("TEMPERATURE", "0"))
    metric = "relevancy"
    os.makedirs("tmp", exist_ok=True)

    current_date = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    root_abspath = "../../data/10_output_pipeline/12-relevancy"
    file_name = os.getenv("DATA_SOURCE_NAME_RELEVANCY")

    data_path = os.path.abspath(f"{root_abspath}/input/{file_name}")

    is_tmp_empty = len(glob.glob(f"tmp/tmp_{metric}.pkl")) == 0

    if is_tmp_empty:
        data_path = os.path.abspath(f"{root_abspath}/input/{file_name}")

        input_data = pd.read_json(data_path)

    else:
        input_data = pd.read_pickle(f"tmp/tmp_{metric}.pkl")

    augmented_with_llm_data, model = run_llm_as_judge(
        input_data,
        metric,
        batch_size,
        model_name,
        temperature,
    )

    save_postprocessed_data(
        augmented_with_llm_data,
        postprocess_output_llm_as_judge,
        metric,
        root_abspath,
        current_date,
    )

    save_metric_results(
        augmented_with_llm_data,
        compute_metric_score,
        metric,
        model,
        root_abspath,
        current_date,
        model_name,
        temperature,
    )

    os.remove(f"tmp/tmp_{metric}.pkl")
