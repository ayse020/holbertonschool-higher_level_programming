#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    
    Args:
        matrix: A list of lists containing integers
                Default is an empty matrix [[]]
    """
    for row in matrix:
        for i in range(len(row)):
            # Use str.format() to print integer without casting to string
            print("{:d}".format(row[i]), end="")
            
            # Add space between elements, but not after the last one
            if i != len(row) - 1:
                print(" ", end="")
        print()
