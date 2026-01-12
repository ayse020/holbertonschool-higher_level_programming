#!/usr/bin/python3
"""This module defines a Rectangle class."""


class Rectangle:
    """Rectangle class with width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)])

    def __repr__(self):
        """Return a formal string representation of the rectangle."""
        return f"Rectangle({self.width}, {self.height})"
