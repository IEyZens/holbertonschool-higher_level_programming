#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Check if the tuples are empty and assign default values
    if len(tuple_a) > 0:
        # Assign the first element of tuple_a to a1
        a1 = tuple_a[0]
    # If tuple_a is empty, assign 0 to a1
    else:
        # Assign 0 to a1
        a1 = 0
    # Check if the second element of tuple_a exists
    if len(tuple_a) > 1:
        # Assign the second element of tuple_a to a2
        a2 = tuple_a[1]
    # If the second element of tuple_a does not exist, assign 0 to a2
    else:
        # Assign 0 to a2
        a2 = 0
    # Check if the first element of tuple_b exists
    if len(tuple_b) > 0:
        # Assign the first element of tuple_b to b1
        b1 = tuple_b[0]
    # If the first element of tuple_b does not exist, assign 0 to b1
    else:
        # Assign 0 to b1
        b1 = 0
    # Check if the second element of tuple_b exists
    if len(tuple_b) > 1:
        # Assign the second element of tuple_b to b2
        b2 = tuple_b[1]
    # If the second element of tuple_b does not exist, assign 0 to b2
    else:
        # Assign 0 to b2
        b2 = 0
    # Return a tuple with the sum of the first elements and the sum of the second elements
    return (a1 + b1, a2 + b2)
