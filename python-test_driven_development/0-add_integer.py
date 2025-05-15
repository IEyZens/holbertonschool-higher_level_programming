#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
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
