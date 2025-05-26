#!/usr/bin/python3
"""Defines a function that checks if an object inherits from a specified class.
    the object.
    """


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited (directly
    or indirectly)
    Args:
        obj: The object to inspect.
        a_class: The class to check against.
    Returns:
        bool: True if obj is an instance of a_class that inherited (directly
        or indirectly)
              from a_class, otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
