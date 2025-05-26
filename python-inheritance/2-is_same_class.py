#!/usr/bin/python3
"""Defines a function that returns a list of available attributes and methods of an object.
    the object.
    """


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    # Check if the object is exactly an instance of the specified class.
    if type(obj) is a_class:
        return True
    else:
        return False
