#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Delete the item at a specific index in a list
    if idx < 0:
        # If the index is negative, return the list unchanged
        return my_list
    # If the index is valid, delete the item at that index
    if idx < len(my_list):
        # Delete the item at the specified index
        del my_list[idx]
    # If the index is out of range, return the list unchanged
    else:
        # If the index is greater than the length of the list, return the list unchanged
        return my_list
    # Return the modified list
    return my_list
