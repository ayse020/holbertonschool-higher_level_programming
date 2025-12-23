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
