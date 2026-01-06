#!/usr/bin/python3
"""
4-print_square module
Defines a function that prints a square with the character #
"""


def print_square(size):
    """
    Prints a square with the character #
    
    Args:
        size (int): The size length of the square
        
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    # Check if size is not an integer (including floats)
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Print the square
    for i in range(size):
        print("#" * size)
    
    # For size = 0, print a blank line to match the test expectation
    if size == 0:
        print()
