#!/usr/bin/python3

def element_at(my_list, idx):
    # Check if the index is negative or out of range
    if idx < 0:
        # Return None if the index is negative
        return None
    # Check if the index is greater than or equal to the length of the list
    elif idx >= len(my_list):
        # Return None if the index is out of range
        return None
    # If the index is valid, return the element at that index
    else:
        # Return the element at the specified index
        return my_list[idx]
