#!/usr/bin/python3
"""
This module provides a function to append a string to a UTF-8 text file
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a UTF-8 text file and returns the number of
    characters added.

    If the file does not exist, it is created. The content is added without
    erasing the previous data.

    Args:
        filename (str): The path to the text file.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.
    """
    # Open the file with the specified filename in append mode
    # and ensure it is encoded in UTF-8.
    with open(filename, "a", encoding="utf-8") as file:
        # Append the text to the file and return the number of characters
        # added.
        return file.write(text)
