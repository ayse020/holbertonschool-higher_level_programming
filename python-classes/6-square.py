#!/usr/bin/python3
"""Module that defines a Square with size and position"""


class Square:
    """Represents a square with size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square
        Args:
            size (int): size of the square
            position (tuple): coordinates for printing
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character considering position"""
        if self.__size == 0:
            print()
            return

        # print vertical offset
        for _ in range(self.__position[1]):
            print()

        # print each row
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
