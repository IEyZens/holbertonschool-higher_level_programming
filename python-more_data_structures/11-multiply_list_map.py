#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Create a new list by multiplying each element in my_list by number
    return list(map(lambda x: x * number, my_list))
