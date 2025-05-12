#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    # Check if the index is negative or out of range
    if idx < 0:
        # Return the original list if the index is negative
        return my_list
    # Check if the index is greater than or equal to the length of the list
    elif idx >= len(my_list):
        # Return the original list if the index is out of range
        return my_list
    # If the index is valid, replace the element at that index
    else:
        # Replace the element at the specified index with the new element
        my_list[idx] = element
        # Return the modified list
        return my_list
