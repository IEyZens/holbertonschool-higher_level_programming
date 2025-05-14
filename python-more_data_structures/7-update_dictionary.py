#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Check if the key exists in the dictionary
    a_dictionary[key] = value
    # If the key does not exist, it will be added with the given value
    return a_dictionary
