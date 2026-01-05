#!/usr/bin/python3
"""
Module: 1-write_file.py
Contains function that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8).
    Returns number of characters written.

    Args:
        filename (str): The name/path of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
