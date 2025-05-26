#!/usr/bin/python3
"""
This module defines a class BaseGeometry with methods for area calculation
and integer validation.
"""


class BaseGeometry:
    """
    A class representing geometric concepts with methods for area calculation
    and integer validation.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.

        Raises:
            Exception: Always, indicating the method is not yet implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    bg = BaseGeometry()
    bg.integer_validator("size", 10)
