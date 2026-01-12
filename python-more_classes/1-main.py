#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

# Create a rectangle with width=2 and height=4
my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)  # Should show: {'_Rectangle__width': 2, '_Rectangle__height': 4}

# Update width and height
my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)  # Should show: {'_Rectangle__width': 10, '_Rectangle__height': 3}
