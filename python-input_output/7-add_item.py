#!/usr/bin/python3
"""7-add_item.py module."""
import sys
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Əgər fayl varsa, ondan oxu
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Bütün argumentləri list-ə əlavə et
my_list.extend(sys.argv[1:])

# List-i fayla yaz
save_to_json_file(my_list, filename)
