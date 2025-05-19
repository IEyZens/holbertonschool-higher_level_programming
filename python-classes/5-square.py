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

    """
    This method calculates the area of the square.
    Returns:
        int: The area of the square.
    """
    def area(self):
        # Calculate the area of the square
        return self.__size * self.__size

    """
    This method returns the string representation of the square.
    Returns:
        str: The string representation of the square.
    """
    @property
    # This method returns the size of the square.
    def size(self):
        # Return the size of the square
        return self.__size

    """
    This method sets the size of the square.
    Args:
        value (int): The new size of the square.
    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
    """
    @size.setter
    # This method sets the size of the square.
    def size(self, value):
        # Check if value is an integer
        if not isinstance(value, int):
            # raise an exception if value is not an integer
            raise TypeError("size must be an integer")
        # Check if value is less than 0
        if value < 0:
            # raise an exception if value is less than 0
            raise ValueError("size must be >= 0")
        # Set the size of the square
        self.__size = value

    """
    This method prints the square using the '#' character.
    If the size is 0, it prints an empty line.
    """
    def my_print(self):
        # Print the square using the '#' character
        if self.__size == 0:
            # If the size is 0, print an empty line
            print()
            # Return from the method
            return
        # Loop through the range of the size
        for i in range(self.__size):
            # Print the '#' character for the size of the square
            print("#" * self.__size)
