#!/usr/bin/python3
"""
Matrix Division Module
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    """
    
    # Error message constants
    MATRIX_TYPE_ERROR = "matrix must be a matrix (list of lists) of integers/floats"
    ROW_SIZE_ERROR = "Each row of the matrix must have the same size"
    DIV_TYPE_ERROR = "div must be a number"
    DIV_ZERO_ERROR = "division by zero"
    
    # Step 1: Validate matrix structure
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(MATRIX_TYPE_ERROR)
    
    # Step 2: Validate each row and elements
    row_length = None
    for row in matrix:
        # Check if row is a list
        if not isinstance(row, list):
            raise TypeError(MATRIX_TYPE_ERROR)
        
        # Check if row is empty
        if len(row) == 0:
            raise TypeError(MATRIX_TYPE_ERROR)
        
        # Check if all rows have the same length
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError(ROW_SIZE_ERROR)
        
        # Check if all elements are integers or floats
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(MATRIX_TYPE_ERROR)
    
    # Step 3: Validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError(DIV_TYPE_ERROR)
    
    # Step 4: Check for division by zero
    if div == 0:
        raise ZeroDivisionError(DIV_ZERO_ERROR)
    
    # Step 5: Perform division and create new matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Divide and round to 2 decimal places
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    
    return new_matrix
