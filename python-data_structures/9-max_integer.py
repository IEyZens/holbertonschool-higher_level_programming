#!/usr/bin/python3

def max_integer(my_list=[]):
    # Loop through the list
    if my_list == []:
        # If the list is empty, return None
        return None
    # Initialize max_val to the first element of the list
    max_val = my_list[0]
    # Loop through the list
    for i in my_list:
        # Compare each element with max_val
        if i > max_val:
            # If i is greater, update max_val
            max_val = i
    # Return the maximum value found
    return max_val
