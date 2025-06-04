#!/usr/bin/python3
"""
This module provides a function to load a Python object
from a JSON-formatted text file.
"""
import json


def load_from_json_file(filename):
    """
    Loads a Python object from a text file containing a JSON representation.

    Args:
        filename (str): The name of the file to read the JSON content from.

    Returns:
        object: The Python object reconstructed from the JSON file.
    """
    with open(filename, encoding="utf-8") as file:
        my_str = json.load(file)
        return my_str
