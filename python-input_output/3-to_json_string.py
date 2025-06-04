#!/usr/bin/python3
"""
This module provides a function that returns the JSON representation of a
Python object as a string.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of a Python object as a string.

    Args:
        my_obj: The Python object to be serialized to JSON format.

    Returns:
        str: A string containing the JSON representation of the object.
    """
    # Use the json.dumps() function to convert the Python object to a JSON
    # string.
    json_str = json.dumps(my_obj)
    # Return the JSON string.
    return json_str
