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
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"
    row_err = "Each row of the matrix must have the same size"
    div_err = "div must be a number"
    zero_err = "division by zero"

    # Check if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError(matrix_err)
    
    # Check if matrix is empty
    if len(matrix) == 0:
        raise TypeError(matrix_err)
    
    # Check each row
    for row in matrix:
        # Check if row is a list
        if not isinstance(row, list):
            raise TypeError(matrix_err)
        # Check if row is empty
        if len(row) == 0:
            raise TypeError(matrix_err)
        # Check each element in row
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(matrix_err)
    
    # Check if all rows have the same size
    # First check if we have at least one row with elements
    if len(matrix[0]) == 0:
        raise TypeError(matrix_err)
    
    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
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
            # Handle division by infinity
            result = element / div
            # Round to 2 decimal places
            new_row.append(round(result, 2))
        new_matrix.append(new_row)
    
    return new_matrix
