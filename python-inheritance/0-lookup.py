#!/usr/bin/python3
"""Defines a function that returns a list of available attributes and methods of an object.
    the object.
    """


def lookup(obj):
    """Return a list of available attributes and methods of an object.
    Args:
        obj: The object to inspect.
    Returns:
        list: A list of strings representing the attributes and methods of the object.
    """
    # Return a list of available attributes and methods of an object.
    return dir(obj)
