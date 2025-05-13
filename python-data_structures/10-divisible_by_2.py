#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create a new list to store the results
    new_list = []
    # Loop through the list
    for i in my_list:
        # Check if the integer is divisible by 2
        if i % 2 == 0:
            # Append True to the new list if divisible by 2
            new_list.append(True)
        # Append False to the new list if not divisible by 2
        else:
            # Append False to the new list
            new_list.append(False)
    # Return the new list
    return new_list
