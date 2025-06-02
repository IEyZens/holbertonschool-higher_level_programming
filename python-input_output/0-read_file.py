#!/usr/bin/python3
"""
This module provides a function to read and print the content of a UTF-8 text
file.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str): The path to the text file to be read.
    """
    # Open the file in read mode using 'with' to ensure it is properly closed
    with open(filename, encoding="utf-8") as file:
        # Read the full content of the file
        content = file.read()
        # Print the content to standard output
        print(content)
