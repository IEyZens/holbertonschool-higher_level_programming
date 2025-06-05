#!/usr/bin/python3
"""
This module defines a function that generates Pascal's triangle
up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the n-th row.

    Each row is represented as a list of integers, and the triangle
    is returned as a list of these rows.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              Returns an empty list if n <= 0.
    """
    # Initialize the triangle with the first row
    my_list = [[1]]
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        # Return an empty list if n is not positive
        return []

    # Generate each row of Pascal's triangle
    # Starting from the second row (index 1) up to n-1
    # Each row is generated based on the previous row
    # The first and last elements of each row are always 1
    for i in range(1, n):
        # Get the last row from the triangle
        prev = my_list[-1]
        # Create a new row starting with 1
        new = [1]
        # Calculate the middle elements of the new row
        for j in range(1, len(prev)):
            # Each middle element is the sum of the two elements
            new.append(prev[j - 1] + prev[j])
        # End the new row with 1
        new.append(1)
        # Append the newly created row to the triangle
        my_list.append(new)
    # Return the complete triangle as a list of lists
    return my_list
