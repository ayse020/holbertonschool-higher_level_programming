#!/usr/bin/python3
"""
0-add_integer module
Function that adds two integers
"""


def add_integer(a, b=98):
    """
    Returns the addition of two integers

    Args:
        a: first number (int or float)
        b: second number (int or float), defaults to 98

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b is not int or float
        OverflowError: for float('inf') or float('-inf')
        ValueError: for float('nan')
    """
    # Type checking first
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    # Handle special float cases before conversion
    # Check for NaN (Not a Number) - nan is not equal to itself
    if isinstance(a, float) and a != a:
        raise ValueError("cannot convert float NaN to integer")

    if isinstance(b, float) and b != b:
        raise ValueError("cannot convert float NaN to integer")

    # Check for infinity
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")

    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise OverflowError("cannot convert float infinity to integer")

    # Convert to integers (safe now)
    a = int(a)
    b = int(b)

    # Return sum
    return a + b
