#!/usr/bin/python3
"""
This module defines a function to print a formatted name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name in the format: My name is <first name> <last name>.

    Args:
        first_name: The first name (must be a string).
        last_name: The last name (optional, must be a string).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        # Check if first_name is a string
        raise TypeError("first_name must be a string")
    # Check if last_name is a string
    if not isinstance(last_name, str):
        # Check if last_name is a string
        raise TypeError("last_name must be a string")

    # Print the full name
    print(f"My name is {first_name} {last_name} ".strip())
