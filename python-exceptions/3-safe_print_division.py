#!/usr/bin/python3

def safe_print_division(a, b):
    # Prints the result of the division of a by b
    result = None
    # Try to perform the division
    try:
        # Check if b is not zero
        result = a / b
    # If b is zero, catch the ZeroDivisionError
    except ZeroDivisionError:
        # Print a message indicating that the division by zero is not allowed
        pass
    # If the division is successful, print the result
    finally:
        # Print the result of the division
        if result is None:
            # Print a message indicating that the result is None
            print("Inside result: None")
        # If the division is successful, print the result
        else:
            # Print the result of the division
            print("Inside result: {}".format(result))
    # Return the result of the division
    return result
