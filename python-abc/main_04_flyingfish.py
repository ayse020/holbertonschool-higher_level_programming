#!/usr/bin/env python3
"""
Test file for Task 4
"""
from task_04_flyingfish import FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()

print(FlyingFish.__mro__)
