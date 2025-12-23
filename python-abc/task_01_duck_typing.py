#!/usr/bin/env python3
"""
Task 1: Shapes with Duck Typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all shapes.
    This class cannot be instantiated directly.
    """
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    Represents a circle with a given radius.
    """
    
    def __init__(self, radius):
        """
        Initialize a circle with given radius.
        
        Args:
            radius (float): Radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate area of circle.
        Formula: π * r²
        
        Returns:
            float: Area of the circle
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate perimeter (circumference) of circle.
        Formula: 2 * π * r
        
        Returns:
            float: Perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    Represents a rectangle with given width and height.
    """
    
    def __init__(self, width, height):
        """
        Initialize a rectangle with given width and height.
        
        Args:
            width (float): Width of the rectangle
            height (float): Height of the rectangle
        """
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate area of rectangle.
        Formula: width * height
        
        Returns:
            float: Area of the rectangle
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate perimeter of rectangle.
        Formula: 2 * (width + height)
        
        Returns:
            float: Perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function that demonstrates duck typing.
    It works with any object that has area() and perimeter() methods.
    
    Args:
        shape: Any object with area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
