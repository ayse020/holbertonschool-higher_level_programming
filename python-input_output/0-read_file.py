#!/usr/bin/python3
"""
Module: 0-read_file.py
Contains function that reads a text file and prints it to stdout.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    
    Args:
        filename (str): The name/path of the file to read.
    
    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content, end='')
