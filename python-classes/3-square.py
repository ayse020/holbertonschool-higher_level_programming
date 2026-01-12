#!/usr/bin/python3
"""Module that defines a Square with size and area method"""


class Square:
    """Square class with private size and public area method"""

    def __init__(self, size=0):
        """Initialize a square with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size
