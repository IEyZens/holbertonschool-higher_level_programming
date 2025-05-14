#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    new_matrix = []
    # Iterate through each row of the input matrix
    for row in matrix:
        # Create a new row for the new matrix
        square_line = []
        # Iterate through each element in the row
        for j in row:
            # Append the square of the element to the new row
            square_line.append(j ** 2)
        # Append the new row to the new matrix
        new_matrix.append(square_line)
    # Return the new matrix with squared elements
    return new_matrix
