#!/usr/bin/python3
"""
matrix_divided module
Defines a function to divide all elements of a matrix by a given divisor
"""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimal places"""

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all elements are int or float
    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows are of the same size
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Ch
