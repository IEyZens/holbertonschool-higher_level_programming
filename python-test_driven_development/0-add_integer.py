#!/usr/bin/python3
"""
This module provides a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (which are first cast to integers).

    Args:
        a: An integer or float.
        b: An integer or float (default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not integers or floats.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100)
        198
    """

    # Validate the input types
    if not isinstance(a, (int, float)):
        # Check if a is an integer or float
        raise TypeError("a must be an integer")
    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        # Check if b is an integer or float
        raise TypeError("b must be an integer")

    # Convert float to int
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
