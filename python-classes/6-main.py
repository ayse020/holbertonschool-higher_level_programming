#!/usr/bin/python3
"""6-square.py: Square class with size and position"""

class Square:
    """Defines a square with size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with optional size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with type and value validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with type and value validation"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' considering position"""
        if self.__size == 0:
            print("")
            return

        # print newlines for vertical position
        for _ in range(self.__position[1]):
            print("")

        # print each row of square with horizontal position offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
