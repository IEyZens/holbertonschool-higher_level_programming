#!/usr/bin/python3
"""
This module provides a function to convert CSV data into JSON format.

It reads a CSV file, parses its rows into dictionaries,
and writes the resulting data to a JSON file called 'data.json'.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Converts the contents of a CSV file to JSON format and writes it
    to 'data.json'.

    Args:
        filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if the conversion is successful, False if an error occurs.
    """
    # Ensure the filename is a string and not empty
    try:
        # Open the CSV file and read its content
        with open(filename, "r", encoding="utf-8") as file:
            # Use csv.DictReader to parse the CSV file into a list of
            # dictionaries
            dict = csv.DictReader(file)
            # Convert the DictReader object to a list of dictionaries
            data = list(dict)

        # Write the list of dictionaries to a JSON file
        with open("data.json", "w") as file:
            # Serialize the list of dictionaries to JSON and write it to the
            # file
            json.dump(data, file, indent=4)
        # Return True to indicate successful conversion
        return True
    # Handle any exceptions that occur during file operations
    except Exception:
        # Print an error message for debugging purposes
        return False
