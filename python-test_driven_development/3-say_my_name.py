#!/usr/bin/python3
"""
This module contains a function that prints a formatted name string.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'
    
    Args:
        first_name (str): First name
        last_name (str, optional): Last name. Defaults to "".
    
    Raises:
        TypeError: If first_name or last_name is not a string
    
    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        
        >>> say_my_name("Walter", "White")
        My name is Walter White
        
        >>> say_my_name("Bob")
        My name is Bob
    """
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print the formatted message
    # Using .rstrip() to remove trailing space when last_name is empty
    print(f"My name is {first_name} {last_name}".rstrip())


# Test the function if script is run directly
if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except Exception as e:
        print(e)
