#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

# iki rectangle yaradırıq
my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)

# neçə obyekt olduğunu göstər
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

# birini silirik
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

# ikinciyi silirik
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
