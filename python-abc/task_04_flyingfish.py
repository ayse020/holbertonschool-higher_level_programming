#!/usr/bin/env python3
"""The Enigmatic FlyingFish - Exploring Multiple Inheritance"""

class Fish:
    """Fish class representing aquatic animals"""
    
    def swim(self):
        """Print swimming message"""
        print("The fish is swimming")
    
    def habitat(self):
        """Print habitat message"""
        print("The fish lives in water")

class Bird:
    """Bird class representing aerial animals"""
    
    def fly(self):
        """Print flying message"""
        print("The bird is flying")
    
    def habitat(self):
        """Print habitat message"""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
    FlyingFish class that inherits from both Fish and Bird
    Demonstrates multiple inheritance in Python
    """
    
    def fly(self):
        """Override Bird's fly method for flying fish"""
        print("The flying fish is soaring!")
    
    def swim(self):
        """Override Fish's swim method for flying fish"""
        print("The flying fish is swimming!")
    
    def habitat(self):
        """Override habitat method for flying fish"""
        print("The flying fish lives both in water and the sky!")
