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

    def __str__(self):
        """Returns a string representation of the rectangle."""
        # Return a string representation of the rectangle in the format:
        # "[Rectangle] width/height".
        # This method overrides the default string representation to provide
        # a more informative output.
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Calculates the area of the rectangle."""
        # Calculate the area of the rectangle by multiplying its width and hei
        # This method overrides the area method from BaseGeometry to provide
        # a specific implementation for rectangles.
        # The area is computed as width multiplied by height.
        return self.__width * self.__height
