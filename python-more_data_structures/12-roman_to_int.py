#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev = 0
    for char in reversed(roman_string):
        val = roman_values.get(char)
        if val is None:
            return 0
        if val < prev:
            total -= val
        else:
            total += val
            prev = val
    return total
