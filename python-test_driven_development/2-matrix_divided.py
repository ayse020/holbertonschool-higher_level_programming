#!/usr/bin/python3
"""
Matrix Division Module
This module provides a function to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number.

    Args:
        matrix: List of lists containing integers or floats
        div: Number to divide by (integer or float)

    Returns:
        New matrix with all elements divided by div,
        rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows have different sizes, or if div is not a number
        ZeroDivisionError: If div is zero
    """
    # Check if matrix is a list
    if not isinstance(matrix, list) or len(matrix) == 0:
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)

    # Check if all rows are lists and not empty
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            msg = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(msg)

    # Check if all elements are integers or floats
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                msg = "matrix must be a matrix (list of lists)"
                msg += " of integers/floats"
                raise TypeError(msg)

    # Check if all rows have the same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            msg = "Each row of the matrix must have the same size"
            raise TypeError(msg)

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Handle division by infinity
    if div == float('inf') or div == float('-inf'):
        return [[0.0 for _ in row] for row in matrix]

    # Perform division and round to 2 decimal places
    result = []
    for row in matrix:
        new_row = []
        for element in row:
            divided = element / div
            rounded = round(divided, 2)
            new_row.append(rounded)
        result.append(new_row)

    return result
