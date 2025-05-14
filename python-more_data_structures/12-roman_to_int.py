#!/usr/bin/python3

def roman_to_int(roman_string):
    # Convert a Roman numeral string to an integer.
    if not isinstance(roman_string, str):
        # If the input is not a string, return 0
        return 0

    # Define a dictionary to map Roman numerals to their integer values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev = 0
    # Iterate through the Roman numeral string in reverse order
    for char in reversed(roman_string):
        # Get the integer value of the current Roman numeral
        val = roman_values.get(char)
        # If the character is not a valid Roman numeral, return 0
        if val is None:
            # If the character is not valid, return 0
            return 0
        # If the current value is less than the previous value, subtract it from the total
        if val < prev:
            # If the current value is less than the previous value, subtract it from the total
            total -= val
        # Otherwise, add it to the total
        else:
            # If the current value is greater than or equal to the previous value, add it to the total
            total += val
            # Update the previous value to the current value for the next iteration
            prev = val
    # Return the total integer value of the Roman numeral string
    return total
