#!/usr/bin/python3
"""4-square.py: Square with size getter and setter"""


class Square:
    """Square class with private size attribute and area method"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): size of the square
        """
        self.size = size  # <- will call the setter

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2
