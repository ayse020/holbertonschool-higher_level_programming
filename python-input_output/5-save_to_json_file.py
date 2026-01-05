#!/usr/bin/python3
"""5-save_to_json_file.py module."""
import json


def save_to_json_file(my_obj, filename):
    """Write object to file in JSON format."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
