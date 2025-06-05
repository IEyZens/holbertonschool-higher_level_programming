#!/usr/bin/python3
"""
This module provides basic serialization and deserialization
functions for handling Python dictionaries with JSON files.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The name of the file to save the JSON content to.

    This function overwrites the file if it already exists.
    """
    # Ensure the data is a dictionary
    with open(filename, "w", encoding="utf-8") as file:
        # Serialize the dictionary to JSON and write it to the file
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes its content into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        dict: The Python dictionary resulting from the JSON content.
    """
    # Open the file and read its content
    with open(filename, "r", encoding="utf-8") as file:
        # Deserialize the JSON content into a Python dictionary
        new_dic = json.load(file)
        # Return the deserialized dictionary
        return new_dic
