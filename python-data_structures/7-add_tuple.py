#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise.
    
    Args:
        tuple_a: First tuple (default empty)
        tuple_b: Second tuple (default empty)
    
    Returns:
        A tuple with 2 integers containing the sum of corresponding elements
    """
    # Ensure both tuples have at least 2 elements (fill with 0 if needed)
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Use only first 2 elements and calculate sum
    return (a[0] + b[0], a[1] + b[1])
