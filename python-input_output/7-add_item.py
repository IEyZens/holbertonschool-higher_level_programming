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

filename = "add_item.json"
args = sys.argv[1:]

if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, filename)
