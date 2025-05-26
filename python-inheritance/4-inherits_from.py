#!/usr/bin/python3
"""Defines a function that checks if an object inherits from a specified class.
    the object.
    """


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited (directly or indirectly)
    Args:
        obj: The object to inspect.
        a_class: The class to check against.
    Returns:
        bool: True if obj is an instance of a_class that inherited (directly or indirectly)
              from a_class, otherwise False.
    """
    # Check if obj is an instance of a_class that inherited (directly or indirectly)
    if isinstance(obj, a_class) and type(obj) is not a_class:
        # Return True if obj is an instance of a_class that inherited (directly or indirectly)
        return True
    # Check if obj is not an instance of a_class, but is an instance of a subclass of a_class
    else:
        # Return False if obj is not an instance of a_class that inherited (directly or indirectly)
        return False
