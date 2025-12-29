#!/usr/bin/python3
"""
Matrix Division Module

This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists containing integers or floats
        div: A number (integer or float) to divide by

    Returns:
        A new matrix with all elements divided by div,
        rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows have different sizes,
                   or if div is not a number
        ZeroDivisionError: If div is zero
    """
    # Error messages
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"
    row_err = "Each row of the matrix must have the same size"
    div_err = "div must be a number"
    zero_err = "division by zero"

    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(matrix_err)

    # Check if matrix is empty
    if not matrix:
        raise TypeError(matrix_err)

    # Check each row
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_err)
        if not row:
            raise TypeError(matrix_err)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(matrix_err)

    # Check if all rows have the same size
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(row_err)

    # Check divisor
    if not isinstance(div, (int, float)):
        raise TypeError(div_err)

    if div == 0:
        raise ZeroDivisionError(zero_err)

    # Perform division and rounding
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = element / div
            rounded = round(result, 2)
            # Handle -0.0 case
            if rounded == -0.0:
                rounded = 0.0
            new_row.append(rounded)
        new_matrix.append(new_row)

    return new_matrix
