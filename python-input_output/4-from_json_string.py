#!/usr/bin/python3
"""
This module provides a function that returns a Python object
from its JSON string representation.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): A string containing a JSON representation of an object.

    Returns:
        object: The Python data structure corresponding to the JSON string.
    """
    # Use the json.loads() function to parse the JSON string
    # and convert it into a Python object.
    json_str = json.loads(my_str)
    # Return the Python object.
    # This could be a dictionary, list, string, number, etc.
    # depending on the content of the JSON string.
    return json_str
