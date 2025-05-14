#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same dimensions as the input matrix
    return list(map(lambda i: list(map(lambda j: j ** 2, i)), matrix))
