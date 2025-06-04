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
    # Open the file with the specified filename in read mode
    # and ensure it is encoded in UTF-8.
    with open(filename, encoding="utf-8") as file:
        # Load the JSON content from the file and return the
        # corresponding Python object.
        # The json.load function reads the file and parses the JSON data,
        # converting it into a Python object (like a dictionary or list).
        # The file is expected to contain a valid JSON string.
        # The file is automatically closed after the with block.
        my_str = json.load(file)
        # Return the Python object loaded from the JSON file.
        return my_str
