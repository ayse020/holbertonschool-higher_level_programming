#!/usr/bin/python3
"""
Lazy Matrix Multiplication using NumPy

This module provides a function to multiply two matrices using NumPy.
The function includes comprehensive input validation and returns
appropriate error messages if the input matrices are invalid.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    
    Args:
        m_a: First matrix (list of lists of integers/floats)
        m_b: Second matrix (list of lists of integers/floats)
    
    Returns:
        The product of m_a and m_b as a list of lists
    
    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, 
                   or contains non-numeric elements
        ValueError: If m_a or m_b is empty, has rows of different sizes,
                    or matrices cannot be multiplied
    """
    
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    
    for row in m_a:
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
    
    # Check all elements in m_a are integers or floats
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    
    # Check all rows in m_a have the same size
    first_row_len = len(m_a[0])
    for row in m_a:
        if len(row) != first_row_len:
            raise TypeError("each row of m_a must be of the same size")
    
    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    for row in m_b:
        if len(row) == 0:
            raise ValueError("m_b can't be empty")
    
    # Check all elements in m_b are integers or floats
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    
    # Check all rows in m_b have the same size
    first_row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != first_row_len_b:
            raise TypeError("each row of m_b must be of the same size")
    
    # Check if matrices can be multiplied
    # m_a columns must equal m_b rows
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Convert to NumPy arrays and perform multiplication
    np_a = np.array(m_a)
    np_b = np.array(m_b)
    result = np.matmul(np_a, np_b)
    
    # Convert result back to list of lists and return
    return result.tolist()


if __name__ == "__main__":
    # Test the function with the provided examples
    print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
