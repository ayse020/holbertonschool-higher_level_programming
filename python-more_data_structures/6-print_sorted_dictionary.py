#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    # Get sorted keys
    sorted_keys = sorted(a_dictionary.keys())

    # Print each key-value pair
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
