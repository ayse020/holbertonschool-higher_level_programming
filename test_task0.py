#!/usr/bin/python3
import importlib.util
import sys

# Dinamik import
spec = importlib.util.spec_from_file_location("square_matrix_simple", "0-square_matrix_simple.py")
module = importlib.util.module_from_spec(spec)
sys.modules["square_matrix_simple"] = module
spec.loader.exec_module(module)
from square_matrix_simple import square_matrix_simple

# Test 1
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = square_matrix_simple(matrix)
expected = [[1, 4, 9], [16, 25, 36], [49, 64, 81]]

if result == expected:
    print("✓ Test 1 PASSED")
else:
    print("✗ Test 1 FAILED")
    print(f"Got: {result}")
    print(f"Expected: {expected}")

# Test 2 - Original unchanged
if matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
    print("✓ Test 2 PASSED (original unchanged)")
else:
    print("✗ Test 2 FAILED (original was modified)")
