#!/usr/bin/python3

def lookup(obj):
    """Return a list of available attributes and methods of an object.
    Args:
        obj: The object to inspect.
    Returns:
        list: A list of strings representing the attributes and methods of
    """
    # Return a list of available attributes and methods of an object.
    return dir(obj)
