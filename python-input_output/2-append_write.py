#!/usr/bin/python3
"""
Module: 2-append_write.py
Contains function that appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8).
    Returns number of characters added.

    Args:
        filename (str): The name/path of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: Number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
