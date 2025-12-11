#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Print all integers of a list.
    Each integer is printed on a separate line.
    Uses str.format() for printing.
    """
    for num in my_list:
        print("{:d}".format(num))

# Aşağıdakı kod test üçündür, təqdimat zamanı silə bilərsiniz
# if __name__ == "__main__":
#     my_list = [1, 2, 3, 4, 5]
#     print_list_integer(my_list)
