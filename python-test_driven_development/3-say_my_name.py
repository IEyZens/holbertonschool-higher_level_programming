#!/usr/bin/python3
"""Defines a matrix division function."""


def say_my_name(first_name, last_name=""):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    # Check if first_name is a string
    if not isinstance(first_name, (str)):
        # Check if first_name is a string
        raise TypeError("first_name must be a string")
    # Check if last_name is a string
    if not isinstance(last_name, (str)):
        # Check if last_name is a string
        raise TypeError("last_name must be a string")

    # Print the full name
    print(f"My name is {first_name} {last_name}")
