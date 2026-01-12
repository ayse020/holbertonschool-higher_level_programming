#!/usr/bin/python3
"""5-square.py: Square class with size, area, and my_print"""

class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize a square with optional size"""
        self.size = size  # Burada setter çağırılır və validation edilir

    @property
    def size(self):
        """Getter to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to set the size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # character"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print('#' * self.__size)
