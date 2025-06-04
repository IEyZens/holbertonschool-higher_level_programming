#!/usr/bin/python3
"""
This module provides a function to write a string to a UTF-8 text file
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 text file and returns the number of characters
    written.

    If the file already exists, its content is overwritten. If it does not
    exist, the function creates it.

    Args:
        filename (str): The path to the text file.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written to the file.
    """
    # Open the file with the specified filename in write mode
    # and ensure it is encoded in UTF-8.
    with open(filename, "w", encoding="utf-8") as file:
        # Write the text to the file and return the number of characters
        # written.
        return file.write(text)
