#!/usr/bin/python3

def safe_print_integer(value):
    # Prints an integer with "{:d}".format()
    try:
        # Try to print the value as an integer
        print("{:d}".format(value))
    # If the value is not an integer, catch the TypeError
    except (ValueError, TypeError):
        # Print a new line and return False
        return False
    # If the value is an integer, return True
    else:
        # Return True if the value is an integer
        return True
