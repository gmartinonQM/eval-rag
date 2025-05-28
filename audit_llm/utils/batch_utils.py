from typing import Tuple


def get_batch_indices(
    batch_size: int, batch_index: int, n_rows: int
) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a data batch.

    Parameters
    ----------
    batch_size : int
        The number of rows in each batch. If 0, the entire dataset is considered
        as a single batch.
    batch_index : int
        The index of the current batch (0-based).
    n_rows : int
        The total number of rows in the dataset.

    Returns
    -------
    Tuple[int, int]
        A tuple containing the start index and end index
        for the batch.
    """
    start_index = batch_index * batch_size
    end_index = (
        min((batch_index + 1) * batch_size, n_rows)
        if batch_size > 0
        else n_rows
    )

    return start_index, end_index
