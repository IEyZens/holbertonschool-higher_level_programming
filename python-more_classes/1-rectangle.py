#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Set the width of the rectangle
        self.width = width
        # Set the height of the rectangle
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Return the width of the rectangle
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        # Check if value is an integer
        if not isinstance(value, int):
            # raise an exception if value is not an integer
            raise TypeError("width must be an integer")
        # Check if value is less than 0
        if value < 0:
            # raise an exception if value is less than 0
            raise ValueError("width must be >= 0")
        # Set the width of the rectangle
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Return the height of the rectangle
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        # Check if value is an integer
        if not isinstance(value, int):
            # raise an exception if value is not an integer
            raise TypeError("height must be an integer")
        # Check if value is less than 0
        if value < 0:
            # raise an exception if value is less than 0
            raise ValueError("height must be >= 0")
        # Set the height of the rectangle
        self.__height = value
