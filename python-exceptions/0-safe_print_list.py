#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list safely.
    
    Args:
        my_list (list): The list to print elements from
        x (int): The number of elements to print
    
    Returns:
        int: The real number of elements printed
    """
    count = 0
    
    try:
        for i in range(x):
            # Try to access and print each element
            print(my_list[i], end="")
            count += 1
    except IndexError:
        # This exception occurs when we try to access
        # an index that doesn't exist in the list
        pass
    
    print()  # Print new line after all elements
    return count
