#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element in a list.
    
    Args:
        my_list: The initial list
        search: The element to replace
        replace: The new element
    
    Returns:
        A new list with all occurrences of 'search' replaced by 'replace'
    """
    return [replace if element == search else element for element in my_list]
