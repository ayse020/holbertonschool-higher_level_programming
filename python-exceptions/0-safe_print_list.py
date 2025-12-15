def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.
    
    Args:
        my_list (list): The list to print elements from
        x (int): The number of elements to print
        
    Returns:
        int: The real number of elements printed
    """
    printed_count = 0
    
    try:
        for i in range(x):
            # Print each element without newline
            print(my_list[i], end="")
            printed_count += 1
    except IndexError:
        # This happens when x is bigger than the list length
        # We just want to stop printing, no error message needed
        pass
    finally:
        # Always print a new line after all elements
        print()
    
    return printed_count
