#!/usr/bin/python3
"""
Defines a base class for geometric shapes with methods for area calculation
and integer validation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle.
    Inherits from Rectangle and validates the size of the square.
    """

    def __init__(self, size):
        """Initializes a Square instance.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        # Validate the size of the square.
        # using the integer_validator method from BaseGeometry.
        self.integer_validator("size", size)
        super(Square, self).__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square.
        """
        # Return a string representation of the square.
        # The string representation should be in the format:
        # [Square] size/size
        # where size is the size of the square.
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        """Calculate the area of the square.
        Args:
            None
        Returns:
            int: The area of the square.
        Raises:
            None
        """
        # Calculate the area of the square.
        # The area of a square is size * size.
        # Return the area of the square.
        return self.__size * self.__size
