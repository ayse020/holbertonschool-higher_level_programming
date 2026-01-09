#!/usr/bin/python3
"""
This module contains a function text_indentation(text) that prints a text
with 2 new lines after each '.', '?' or ':'. It also raises a TypeError
if the input is not a string.
"""


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
            print(line.strip(), end="\n\n")
            line = ""

    if line:
        print(line.strip(), end="")

