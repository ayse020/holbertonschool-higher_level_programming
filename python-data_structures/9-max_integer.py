#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds the biggest integer in a list.
    
    Args:
        my_list: List of integers to search
    
    Returns:
        int: Maximum integer in the list
        None: If list is empty
    """
    
    # Check if list is empty
    if not my_list:
        return None
    
    # Initialize max with first element
    max_num = my_list[0]
    
    # Iterate through the list
    for num in my_list:
        if num > max_num:
            max_num = num
    
    return max_num
