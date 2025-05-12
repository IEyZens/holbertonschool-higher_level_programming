#!/usr/bin/python3

def no_c(my_string):
    # Create a new string with all 'c' and 'C' characters removed
    result = ""
    # Loop through the original string
    for i in my_string:
        # If the character is not 'c' or 'C', add it to the result
        if i != 'c' and i != 'C':
            # Add the character to the result
            result += i
    # Return the new string
    return result
