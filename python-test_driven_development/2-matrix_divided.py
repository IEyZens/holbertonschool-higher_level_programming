#!/usr/bin/python3

def matrix_divided(matrix, div):
    new_matrix = []
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")
    for row in matrix:
        new_row = []
        if not isinstance(row, (list)):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)
    return new_matrix
