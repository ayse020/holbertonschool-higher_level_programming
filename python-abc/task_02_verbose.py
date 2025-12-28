#!/usr/bin/env python3
"""Extending the Python List with Notifications"""

class VerboseList(list):
    """A list that prints notifications for modifications"""
    
    def append(self, item):
        """Add an item to the end of the list with notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """Extend the list with items from iterable with notification"""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")
    
    def remove(self, item):
        """Remove first occurrence of item with notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """Remove and return item at index with notification"""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
