#!/usr/bin/python3
"""Defines a function that returns a list of available attributes and method
    the object.
    """
# This code defines a class MyList that inherits from the built-in list class.
# It adds a method print_sorted that prints the elements of the list in sorte


class MyList(list):
    """A class that inherits from list and adds a method to print sorted el."""
    def print_sorted(self):
        """Prints the elements of the list in sorted order."""
        print(sorted(self))
