#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' or ':'.
    
    Args:
        text (str): The string to print
    
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    line = ""
    
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            print()
            line = ""
    
    if line:
        print(line.strip())
