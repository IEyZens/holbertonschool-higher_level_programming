#!/usr/bin/python3
"""
Defines a base class for geometric shapes with methods for area calculation
and integer validation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from BaseGeometry.
    This class provides methods to compute the area of the rectangle
    and validate its dimensions.
    """

    def __init__(self, width, height):
        """
        Initializes the BaseGeometry instance with width and height.
        Args:
            width (int): The width of the geometric shape.
            height (int): The height of the geometric shape.
        Raises:
            TypeError: If `width` or `height` is not an integer.
            ValueError: If `width` or `height` is not greater than 0.
        """
        # Validate the width and height using the integer_validator method
        # and set them as private attributes.
        # `width` and `height` must be positive integers.
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
