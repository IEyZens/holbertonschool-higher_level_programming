#!/usr/bin/python3
"""
This module defines a Student class with attributes and a method to return
a JSON-serializable dictionary representation of the instance.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
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
        Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes are included
        in the returned dictionary (if they exist). Otherwise, all attributes
        are returned.

        Args:
            attrs (list or None): Optional list of attribute names to include.

        Returns:
            dict: Dictionary of attributes to be serialized.
        """
        if attrs is None:
            return self.__dict__
        if type(attrs) == list and all(type(a) == str for a in attrs):
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
