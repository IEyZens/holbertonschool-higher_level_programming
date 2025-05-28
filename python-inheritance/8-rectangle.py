#!/usr/bin/python3
"""
Defines a base class for geometric shapes with methods for area calculation
and integer validation.
"""


class BaseGeometry:
    """
    Base class for geometric shapes.
    This class provides methods for validating integers and computing
    the area of geometric shapes.
    """

    def area(self):
        """
        Computes the area of the geometric shape.
        This method is intended to be implemented by subclasses.

        Raises:
            Exception: If the method is not implemented by a subclass.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that `value` is a positive integer.

        Args:
            name (str): The name of the variable to validate.
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


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
