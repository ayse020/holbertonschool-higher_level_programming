#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.
    
    Args:
        matrix: A 2D list of integers
    
    Returns:
        A new matrix with same size where each value is squared
    """
    # Create a new matrix with squared values
    return [[x * x for x in row] for row in matrix]
