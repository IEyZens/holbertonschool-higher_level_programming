#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # Loop through the matrix
    for i in matrix:
        # Loop through each row
        for j in range(len(i)):
            # Print each integer with a space
            if j < len(i) - 1:
                # Print with a space if not the last integer in the row
                print("{:d} ".format(i[j]), end="")
            # Print without a space if the last integer in the row
            else:
                # Print without a space if the last integer in the row
                print("{:d}".format(i[j]), end="")
        # Print a new line after each row
        print()
