#!/usr/bin/env python3
"""
Test file for Task 3
"""
from task_03_counted import CountedIterator

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(item)
except StopIteration:
    print("Iteration stopped")

print(f"Number of items iterated: {counted_iter.get_count()}")
