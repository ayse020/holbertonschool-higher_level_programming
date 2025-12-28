#!/usr/bin/env python3
"""FlyingFish with Multiple Inheritance"""

class Fish:
    """Base class for fish"""
    
    def swim(self):
        """Return swimming message"""
        return "The fish is swimming"
    
    def habitat(self):
        """Return habitat message"""
        return "The fish lives in water"

class Bird:
    """Base class for bird"""
    
    def fly(self):
        """Return flying message"""
        return "The bird is flying"
    
    def habitat(self):
        """Return habitat message"""
        return "The bird lives in the sky"

class FlyingFish(Fish, Bird):
    """FlyingFish inherits from both Fish and Bird"""
    
    def swim(self):
        """Override swim method"""
        return "The flying fish is swimming!"
    
    def fly(self):
        """Override fly method"""
        return "The flying fish is soaring!"
    
    def habitat(self):
        """Override habitat method"""
        return "The flying fish lives both in water and the sky!"
