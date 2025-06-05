#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list,
then saves the list to a file using a JSON representation.

The list is stored in a file named 'add_item.json'.
If the file exists, its content is loaded and extended.
If not, the file is created with the given arguments.
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the filename where the list will be stored
filename = "add_item.json"
# Get the command-line arguments, excluding the script name
args = sys.argv[1:]

# Check if the file exists and load the existing list,
# or create a new list if it doesn't
if os.path.exists(filename):
    # Load the existing list from the JSON file
    # The load_from_json_file function reads the JSON file
    # and returns the corresponding Python object (list).
    # If the file does not exist, it will raise a FileNotFoundError.
    # If the file is empty, it will return an empty list.
    # The file is expected to contain a valid JSON string.
    my_list = load_from_json_file(filename)
# If the file does not exist, create a new empty list
else:
    # Initialize an empty list to store the command-line arguments
    # This list will be used to store the arguments passed to the script.
    my_list = []

# Extend the list with the command-line arguments
my_list.extend(args)
# Save the updated list back to the JSON file
# The save_to_json_file function takes a Python object (in this case, a list)
# and writes it to a file in JSON format.
# It creates the file if it does not exist, or overwrites it if it does.
save_to_json_file(my_list, filename)
