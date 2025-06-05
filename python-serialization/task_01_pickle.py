#!/usr/bin/python3
"""
This module defines a custom Python class with methods
to serialize and deserialize its instances using the pickle module.
"""
import pickle


class CustomObject:
    """
    Represents a custom object with attributes for name, age, and student
    status.

    This class includes methods to display its attributes,
    serialize itself to a file, and load an instance from a file.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance with a name, age, and student
        status.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        # Ensure name is a string
        self.name = name
        # Ensure age is an integer
        self.age = age
        # Ensure is_student is a boolean
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object in a readable format.
        """
        # Display the name of the object
        print(self.name)
        # Display the age of the object
        print(self.age)
        # Display whether the person is a student
        print(self.is_student)

    def serialize(self, filename):
        """
        Serializes the current object and saves it to a file using pickle.

        Args:
            filename (str): The name of the file to save the serialized object
            to.
        """
        # Open the file in binary write mode
        with open(filename, "wb") as file:
            # Use pickle to serialize the object and write it to the file
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from the specified file and returns a
        CustomObject instance.

        Args:
            filename (str): The name of the file to read the serialized object
            from.

        Returns:
            CustomObject or None: The loaded object, or None if loading fails.
        """
        # Attempt to open the file and load the object
        try:
            # Open the file in binary read mode
            with open(filename, "rb") as file:
                # Use pickle to load the object from the file
                new_obj = pickle.load(file)
                # Return the loaded object
                return new_obj
        # Handle exceptions that may occur during file operations or unpickling
        except (FileNotFoundError, pickle.UnpicklingError, Exception):
            # Print an error message if loading fails
            return None
