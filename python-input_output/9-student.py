#!/usr/bin/python3
"""
This module defines a Student class with basic attributes and a method
to retrieve a dictionary representation suitable for JSON serialization.
"""


class Student:
    """
    Represents a student with basic personal information.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary of the instance's attributes.
        """
        return self.__dict__
