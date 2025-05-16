#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
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
    print("My name is {} {}".format(first_name, last_name))
