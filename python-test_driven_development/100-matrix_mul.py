#!/usr/bin/python3
"""
Defines a matrix multiplication function.
"""


def matrix_mul(*args):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        list of lists of ints/floats: The result of the multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   contains non-integer/float elements, or is not rectangular.
        ValueError: If m_a or m_b is empty, or if the matrices cannot be multiplied.
    """
    # Check number of arguments
    if len(args) != 2:
        if len(args) == 1:
            raise TypeError("missing one argument")
        else:
            raise TypeError(f"matrix_mul() takes 2 positional arguments but {len(args)} were given")
    
    m_a, m_b = args[0], args[1]
    
    # Rest of the validation code remains the same
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check multiplication compatibility
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result


if __name__ == "__main__":
    # Run doctest if executed directly
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
