#!/usr/bin/python3
"""
This module multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix

    Returns:
        list of lists: product of matrices

    Raises:
        TypeError: if inputs are invalid
        ValueError: if matrices can't be multiplied

    Examples:
    >>> matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
    [[13, 16]]
    """
    # Validation
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if any(not isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [[]] or m_a == []:
        raise ValueError("m_a can't be empty")
    if m_b == [[]] or m_b == []:
        raise ValueError("m_b can't be empty")
    if any(not all(isinstance(i, (int, float)) for i in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if any(not all(isinstance(i, (int, float)) for i in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if multiplication possible
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply
    result = []
    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            s = 0
            for k in range(len(row)):
                s += row[k] * m_b[k][col]
            new_row.append(s)
        result.append(new_row)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
