import json
import os
from typing import Any


def save_json(
    file_path: str,
    results: dict[str, Any],
    indent: int = 4,
    ensure_ascii: bool = False,
) -> None:
    """
    Save a dictionary as a JSON file.

    Parameters
    ----------
    file_path : str
        The path where the JSON file will be saved.
    results : dict
        The dictionary to be saved as a JSON file.
    indent : int, optional
        The number of spaces for indentation in the JSON file (default is 4).
    ensure_ascii : bool, optional
        If False, non-ASCII characters are preserved (default is False).

    Returns
    -------
    None
    """
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=indent, ensure_ascii=ensure_ascii)


def get_files_by_extension(
    input_folder: str, extensions: list[str]
) -> list[str]:
    """
    Get a list of files with specified extensions from the input folder.

    Parameters
    ----------
    input_folder : str
        The path to the folder containing files.

    extensions : list[str]
        A list of file extensions to filter by (e.g., ['.json', '.txt']).

    Returns
    -------
    list[str]
        A list of file names in the input folder with the specified extensions.

    """
    return [
        file
        for file in os.listdir(input_folder)
        if any(file.endswith(ext) for ext in extensions)
    ]
