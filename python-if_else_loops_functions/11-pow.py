#!/usr/bin/python3
def pow(a, b):
    """Return a to the power of b."""
    result = 1
    for _ in range(abs(b)):
        result *= a
    if b < 0:
        return 1 / result
    return result
