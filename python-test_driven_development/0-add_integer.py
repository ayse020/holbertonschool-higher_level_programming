#!/usr/bin/python3
"""
0-add_integer module
Provides function to add two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        Sum of a and b as integer

    Raises:
        TypeError: If a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()
