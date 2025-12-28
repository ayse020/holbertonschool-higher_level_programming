#!/usr/bin/env python3
"""CountedIterator - Keeping Track of Iteration"""

class CountedIterator:
    """An iterator that counts how many items have been iterated"""
    
    def __init__(self, iterable):
        """Initialize with an iterable"""
        self.iterator = iter(iterable)
        self.counter = 0
    
    def __next__(self):
        """Get the next item and increment counter only if successful"""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise
    
    def __iter__(self):
        """Return self as iterator"""
        return self
    
    def get_count(self):
        """Return the number of items iterated"""
        return self.counter
