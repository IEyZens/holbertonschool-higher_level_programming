#!/usr/bin/python3
"""Defines a matrix division function."""


def say_my_name(first_name, last_name=""):
    """Prints a formatted full name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Prints:
        The full name in the format: "My name is <first_name> <last_name>"
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
    print(f"My name is {first_name} {last_name}".strip())
