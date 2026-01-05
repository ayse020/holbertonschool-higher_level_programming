#!/usr/bin/env python3
"""
Basic serialization module that saves Python dictionaries to JSON files
and loads them back from JSON files.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.
    
    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file to a Python dictionary.
    
    Args:
        filename: The filename of the input JSON file
    
    Returns:
        A Python Dictionary with the deserialized JSON data
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
