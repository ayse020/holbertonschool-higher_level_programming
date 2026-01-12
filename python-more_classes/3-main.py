#!/usr/bin/python3
from rectangle import Rectangle

if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(
        "Area:", my_rectangle.area(),
        "- Perimeter:", my_rectangle.perimeter()
    )
    print(my_rectangle)
    print("--")
    print("##########")
    print("##########")
    print("##########")
    another_rectangle = Rectangle(10, 3)
    print(another_rectangle)
