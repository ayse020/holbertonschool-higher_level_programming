#!/usr/bin/python3
"""
Matrix Division Module
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.
    
    Args:
        matrix: A list of lists of integers/floats
        div: A number (integer or float) to divide by
    
    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places
    
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if each row doesn't have the same size,
                   or if div is not a number
        ZeroDivisionError: If div is 0
    """
    # Step 1: Validate matrix structure
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix) == 0 or all(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Step 2: Check row sizes
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    
    # Step 3: Validate matrix elements
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Step 4: Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Step 5: Perform division with special handling for infinity
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Handle division by infinity
            if isinstance(div, float) and div == float('inf'):
                result = 0.0
            else:
                result = element / div
            new_row.append(round(result, 2))
        new_matrix.append(new_row)
    
    return new_matrix
