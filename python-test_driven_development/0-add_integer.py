#!/usr/bin/python3

def add_integer(a, b=98):
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
