#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    
    Args:
        a_dictionary: Dictionary with integer values
    
    Returns:
        Key with the biggest value, or None if empty
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
