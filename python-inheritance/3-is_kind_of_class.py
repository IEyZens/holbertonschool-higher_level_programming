#!/usr/bin/python3
"""Defines a function that returns a list of available attributes and methods of an object.
    the object.
    """


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or if it is an instance of a class
    that inherited from, a specified class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        bool: True if obj is an instance of a_class or an inherited class,
              False otherwise.
    """
    # Check if the object is an instance of the specified class or an inherited class.
    if isinstance(obj, a_class):
        # Return True if obj is an instance of a_class or an inherited class.
        return True
    # Check if the object is not an instance of the specified class or an inherited class.
    else:
        # Return False if obj is not an instance of a_class or an inherited class.
        return False
