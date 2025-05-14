#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the modified elements
    new_list = []
    # Iterate through each element in the original list
    for i in my_list:
        # If the element matches the search value, replace it with the new value
        if i == search:
            # If the element matches the search value, append the replace value
            new_list.append(replace)
        # If the element does not match, append the original element
        else:
            # append the original element
            new_list.append(i)
    # Return the new list with replaced elements
    return new_list
