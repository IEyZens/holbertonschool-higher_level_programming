#!/usr/bin/python3

def best_score(a_dictionary):
    # Check if the dictionary is empty
    if not a_dictionary:
        # Return None if the dictionary is empty
        return None
    # Find the key with the maximum value in the dictionary
    return max(a_dictionary, key=a_dictionary.get)
