from typing import Any

import numpy as np


def get_metric_rate(data: dict[str, Any], n_rows: int) -> float:
    """
    Calculates the ratio of positive metric labels in the provided data.
    Parameters
    ----------
    data : dict[str, Any]
        Dictionary where each value contains a "label" key with a numeric value.
    n_rows : int
        Total number of rows or items to normalize the metric sum.
    Returns
    -------
    float
        The ratio of the sum of metric labels to the total number of rows.
        Returns 0 if n_rows is 0.
    """
    metric_scores = []
    for _, value in data.items():
        metric_scores.append(value["label"])

    metric_ratio = np.sum(metric_scores) / n_rows if n_rows > 0 else 0

    return metric_ratio
