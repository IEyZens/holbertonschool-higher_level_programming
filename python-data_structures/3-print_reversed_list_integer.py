#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    # Loop through the list in reverse order
    for i in my_list[::-1]:
        # Print each integer
        print("{:d}".format(i))
