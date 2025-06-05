#!/usr/bin/python3
"""
This module provides a function that returns the dictionary representation
of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of a class instance suitable for JSON
    serialization.

    All attributes of the instance must be of serializable types:
    list, dictionary, string, integer, and boolean.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing all the attributes of the object.
    """
    # Check if the object is an instance of a class
    return obj.__dict__
