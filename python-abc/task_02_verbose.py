#!/usr/bin/env python3
"""
Task 2: Extending Python's Built-in List
"""


class VerboseList(list):
    """
    A custom list class that prints notifications when items are added or removed.
    Inherits from Python's built-in list class.
    """
    
    def append(self, item):
        """
        Add an item to the end of the list and print a notification.
        
        Args:
            item: The item to append to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable and print a notification.
        
        Args:
            iterable: An iterable of items to add to the list
        """
        # Get the length before extending to calculate how many items are added
        length_before = len(self)
        super().extend(iterable)
        length_after = len(self)
        items_added = length_after - length_before
        print(f"Extended the list with [{items_added}] items.")
    
    def remove(self, item):
        """
        Remove the first occurrence of the item from the list and print a notification.
        
        Args:
            item: The item to remove from the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """
        Remove and return an item at the given index (default last) and print a notification.
        
        Args:
            index (int, optional): Index of the item to pop. Defaults to -1.
        
        Returns:
            The popped item
        """
        # Get the item before popping to print it
        result = super().pop(index)
        print(f"Popped [{result}] from the list.")
        return result
