#!/usr/bin/python3
"""
Module that defines a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of lists of floats: New matrix with elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   or if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is 0.
    """
    # Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix
    if (not isinstance(matrix, list) or
        any(not isinstance(row, list) for row in matrix) or
        any(not all(isinstance(el, (int, float)) for el in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate all rows have the same size
    row_lengths = [len(row) for row in matrix]
    if not all(length == row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    # Perform division and round to 2 decimal places
    new_matrix = [[round(el / div, 2) for el in row] for row in matrix]

    return new_matrix
