#!/usr/bin/python3
"""Defines a class MyList that inherits from list and adds a method to print the list in sorted order."""

class MyList(list):
    """A class that inherits from list and adds a method to print the list in sorted order."""
    def print_sorted(self):
        """Prints the list in sorted order."""
        # Print the list in sorted order.
        print(sorted(self))
