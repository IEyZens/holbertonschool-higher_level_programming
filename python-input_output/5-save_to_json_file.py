#!/usr/bin/python3
"""
This module provides a function to write a Python object to a text file
in JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using its JSON representation.

    The file is created if it doesn't exist and overwritten if it does.

    Args:
        my_obj: The Python object to be serialized and written to the file.
        filename (str): The name of the file to write the JSON representation
        into.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
