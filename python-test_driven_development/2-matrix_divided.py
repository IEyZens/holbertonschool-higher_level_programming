#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor, must be a non-zero integer or float.

    Returns:
        A new matrix where all elements are divided by div, rounded
        to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   or if div is not an integer or float,
                   or if rows of the matrix are not of the same size.
        ZeroDivisionError: If div is 0.
    """
    new_matrix = []
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if not isinstance(row, (list)):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
