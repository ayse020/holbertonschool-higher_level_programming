#!/usr/bin/env python3
"""
Test file for Task 1
"""
from task_01_duck_typing import Circle, Rectangle, shape_info

# Create a circle with radius 5
circle = Circle(radius=5)

# Create a rectangle with width 4 and height 7
rectangle = Rectangle(width=4, height=7)

# Test shape_info with circle
shape_info(circle)

# Add a blank line for separation
print()

# Test shape_info with rectangle
shape_info(rectangle)
