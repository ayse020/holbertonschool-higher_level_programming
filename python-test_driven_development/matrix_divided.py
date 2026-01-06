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
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = []
        for el in row:
            new_row.append(round(el / div, 2))
        new_matrix.append(new_row)

    return new_matrix

