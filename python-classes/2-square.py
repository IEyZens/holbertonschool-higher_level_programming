#!/usr/bin/python3
"""
This module defines an empty class Square.
It serves as a placeholder for future development.
The class does not contain any attributes or methods.
"""


class Square:
    """This is an empty class that defines a square."""

    def __init__(self, size=0):
        """
        Initialize the square with a given size.
        Args:
            size (int): The size of the square.
        """
        # Check if size is an integer
        if not isinstance(size, int):
            # raise an exception if size is not an integer
            raise TypeError("size must be an integer")
        # Check if size is less than 0
        if size < 0:
            # raise an exception if size is less than 0
            raise ValueError("size must be >= 0")

        # Set the size of the square
        self.__size = size
