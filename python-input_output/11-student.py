#!/usr/bin/python3
"""
This module defines a Student class that supports JSON serialization
and deserialization through to_json() and reload_from_json().
"""


class Student:
    """
    Represents a student with first name, last name, and age,
    and provides methods for JSON serialization and deserialization.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only the specified attributes
        will be included in the dictionary if they exist.
        Otherwise, all attributes are returned.

        Args:
            attrs (list or None): List of attribute names to include.

        Returns:
            dict: Dictionary of selected or all attributes.
        """
        # Check if attrs is a list of strings
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            # Return a dictionary with only the specified attributes
            # that exist in the instance's __dict__
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary where each key is the name of a public
                         attribute and the value is the new value to assign.
        """
        # Iterate over the items in the json dictionary
        # and update the instance's attributes accordingly.
        for key, value in json.items():
            # Use setattr to set the attribute dynamically
            self.__dict__[key] = value
