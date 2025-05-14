#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    # Prints x elements of a list
    printed = 0
    # Loop through the list and print each element
    for i in range(x):
        # Try to print the element at index i
        try:
            # Check if the index is within the range of the list
            print("{:d}".format(my_list[i]), end="")
        # If the index is out of range, catch the IndexError
        except IndexError:
            # Print a new line and break the loop
            break
        # If the index is valid, increment the printed count
        except (ValueError, TypeError):
            # If the element is not an integer, skip it
            pass
        # If the index is valid, increment the printed count
        else:
            # Print the element and increment the printed count
            printed += 1
    # Print a new line after printing the elements
    print()
    return printed
