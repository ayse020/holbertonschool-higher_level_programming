#!/usr/bin/env python3
"""
Task 3: CountedIterator
"""


class CountedIterator:
    """
    An iterator that keeps track of how many items have been iterated over.
    """
    
    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.
        
        Args:
            iterable: Any iterable object (list, tuple, etc.)
        """
        self._iterator = iter(iterable)
        self._counter = 0
    
    def __next__(self):
        """
        Get the next item from the iterator and increment the counter.
        
        Returns:
            The next item from the iterator
            
        Raises:
            StopIteration: When there are no more items
        """
        try:
            item = next(self._iterator)
            self._counter += 1
            return item
        except StopIteration:
            raise
    
    def __iter__(self):
        """
        Return self as the iterator.
        This makes CountedIterator both an iterator and iterable.
        """
        return self
    
    def get_count(self):
        """
        Get the current count of items that have been iterated.
        
        Returns:
            int: The number of items iterated so far
        """
        return self._counter
