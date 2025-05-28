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
