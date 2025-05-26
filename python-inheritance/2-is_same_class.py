#!/usr/bin/python3
"""Defines a class MyList that inherits from list and adds a method to print
the list in sorted order.
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    # Check if obj is exactly an instance of a_class.
    return type(obj) == a_class
