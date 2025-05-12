#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Replace an element in a list at a specific index
    if idx < 0:
        # If the index is negative, return the original list
        return my_list
    # If the index is greater than or equal to the length of the list, return the original list
    elif idx >= len(my_list):
        # If the index is greater than or equal to the length of the list, return the original list
        return my_list
    # If the index is valid, create a copy of the list and replace the element at the specified index
    else:
        # Create a copy of the list and replace the element at the specified index
        copy_list = my_list[:]
        # Replace the element at the specified index with the new element
        copy_list[idx] = element
        # Return the modified copy of the list
        return copy_list
