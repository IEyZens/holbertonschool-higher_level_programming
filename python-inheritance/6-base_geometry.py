#!/usr/bin/python3
"""Defines a class BaseGeometry with a method area that raises an exception."""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area() method."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")
