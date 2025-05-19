#!/usr/bin/python3
"""
This module defines a Square class that supports size and position,
calculates area, and prints a square using the '#' character.
"""


class Square:
    """
    Represents a square with size and position attributes,
    provides area calculation and printing functionality.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a given size.
        Args:
            size (int): The size of the square.
        """
        # Set the size of the square
        self.size = size
        # Set the position of the square
        self.position = position

    def area(self):
        """
        Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        # Calculate the area of the square
        return self.__size * self.__size

    @property
    def size(self):
        """
        Get the current size of the square.
        Returns:
            int: The size of the square.
        """
        # Return the size of the square
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
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

    def my_print(self):
        """
        Print the square using the '#' character.
        The square is printed at the specified position.
        If the size is 0, an empty line is printed.
        """
        # Print the square using the '#' character
        if self.__size == 0:
            # If the size is 0, print an empty line
            print()
            # Return from the method
            return
        for _ in range(self.__position[1]):
            print()
        # Loop through the range of the size
        for i in range(self.__size):
            # Print the '#' character for the size of the square
            print(" " * self.position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        Get the current position of the square.
        Returns:
            tuple: The position of the square.
        """
        # Return the position of the square
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.
        Args:
            value (tuple): The new position of the square.
        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        # Check if value is a tuple of 2 positive integers
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            # raise an exception if value is not a tuple of 2 positive integers
            raise TypeError("position must be a tuple of 2 positive integers")
