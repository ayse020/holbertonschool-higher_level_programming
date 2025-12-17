#!/usr/bin/python3
"""
Text Indentation Module
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'
    
    Args:
        text (str): The text to format
    
    Raises:
        TypeError: If text is not a string
    
    Examples:
        >>> text_indentation("Hello. World? Yes:")
        Hello.
        <BLANKLINE>
        World?
        <BLANKLINE>
        Yes:
        <BLANKLINE>
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Initialize variables
    result = ""
    i = 0
    length = len(text)
    
    while i < length:
        result += text[i]
        
        # Check for special characters
        if text[i] in '.?:':
            result += '\n\n'
            
            # Skip spaces after the special character
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        
        i += 1
    
    # Print the formatted text (strip trailing spaces from lines)
    lines = result.split('\n')
    for line in lines:
        print(line.strip())
