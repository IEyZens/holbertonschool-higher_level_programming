#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the results
    new_dictionary = {}
    # Iterate through each key in the original dictionary
    for key in a_dictionary:
        # Multiply the value by 2 and store it in the new dictionary
        new_dictionary[key] = a_dictionary[key] * 2
    # Return the new dictionary with multiplied values
    return new_dictionary
