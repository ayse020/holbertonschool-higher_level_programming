#!/usr/bin/python3
"""
Say My Name Module
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>"
    
    Args:
        first_name (str): First name
        last_name (str, optional): Last name. Defaults to "".
    
    Raises:
        TypeError: If first_name or last_name are not strings
    
    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter", "White")
        My name is Walter White
        >>> say_my_name("Bob")
        My name is Bob
    """
    # Validate first_name
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Validate last_name
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the full name
    print(f"My name is {first_name} {last_name}".rstrip())
