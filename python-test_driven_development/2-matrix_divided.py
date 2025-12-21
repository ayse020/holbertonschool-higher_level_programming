#!/usr/bin/python3
"""Matrix division module."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix.

    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by (integer/float)

    Returns:
        New matrix with divided values rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not list of lists of integers/floats,
                   or rows have different sizes, or div is not a number
        ZeroDivisionError: If div is zero
    """
    # Error messages
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"

    # Validate matrix is a non-empty list
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(err1)

    # Validate each row is a non-empty list
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(err1)

    # Validate all elements are numbers and rows have same size
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(err2)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(err1)

    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError(err3)

    if div == 0:
        raise ZeroDivisionError(err4)

    # Create new matrix with divided and rounded values
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
