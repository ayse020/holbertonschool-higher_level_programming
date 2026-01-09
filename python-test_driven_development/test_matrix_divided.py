#!/usr/bin/python3
"""
Mini test script for matrix_divided function.
Tests normal and error cases.
"""

from matrix_divided import matrix_divided

# Normal case
try:
    matrix = [[1, 2, 3], [4, 5, 6]]
    print("Normal case:")
    print(matrix_divided(matrix, 3))
except Exception as e:
    print("Error:", e)

# Division by zero
try:
    print("\nDivision by zero case:")
    print(matrix_divided(matrix, 0))
except Exception as e:
    print("Error:", e)

# div is not a number
try:
    print("\ndiv is string case:")
    print(matrix_divided(matrix, "2"))
except Exception as e:
    print("Error:", e)

# matrix is not a list of lists
try:
    print("\nmatrix not list of lists case:")
    print(matrix_divided("not a matrix", 2))
except Exception as e:
    print("Error:", e)

# rows of different sizes
try:
    print("\nRows of different sizes case:")
    print(matrix_divided([[1, 2], [3, 4, 5]], 2))
except Exception as e:
    print("Error:", e)

# elements not int/float
try:
    print("\nElements not int/float case:")
    print(matrix_divided([[1, "2"], [3, 4]], 2))
except Exception as e:
    print("Error:", e)
