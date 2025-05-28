import pandas as pd


def rolling_concatenate_string_dynamic(group: pd.DataFrame) -> pd.Series:
    """
    Concatenates strings in a rolling manner within a DataFrame group.
    Parameters
    ----------
    group : pd.DataFrame
        A DataFrame containing a "sentence" column with strings to concatenate.
    Returns
    -------
    pd.Series
        A Series with concatenated strings for each row in the group.
    """
    values = group["sentence"]
    result = []

    for i in range(len(group)):
        rolling_values = list(values.iloc[0:i])
        concatenated_string = (
            " ".join(rolling_values) if len(rolling_values) > 0 else ""
        )

        result.append(concatenated_string)

    return pd.Series(result, index=group.index)
