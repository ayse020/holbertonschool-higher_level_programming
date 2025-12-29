#!/usr/bin/python3
"""
Matrix division module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number

    Args:
        matrix: list of lists of integers/floats
        div: number (integer or float)

    Returns:
        new matrix with all elements divided by div

    Raises:
        TypeError: if matrix is not list of lists of integers/floats
        TypeError: if each row of matrix doesn't have same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        msg = "matrix must be a matrix "
        msg += "(list of lists) of integers/floats"
        raise TypeError(msg)

    for row in matrix:
        for num in row:
            if not isinstance(num, (int, float)):
                msg = "matrix must be a matrix "
                msg += "(list of lists) of integers/floats"
                raise TypeError(msg)

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
