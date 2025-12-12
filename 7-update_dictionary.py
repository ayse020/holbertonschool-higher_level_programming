#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    
    Args:
        a_dictionary: Dictionary to update
        key: Key to add or replace
        value: Value to set
    
    Returns:
        Updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
