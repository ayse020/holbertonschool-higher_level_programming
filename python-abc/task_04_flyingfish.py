#!/usr/bin/env python3
"""
Task 4: FlyingFish with Multiple Inheritance
"""


class Fish:
    """
    Base class representing a fish.
    """
    
    def swim(self):
        """
        Print that the fish is swimming.
        """
        print("The fish is swimming")
    
    def habitat(self):
        """
        Print the fish's habitat.
        """
        print("The fish lives in water")


class Bird:
    """
    Base class representing a bird.
    """
    
    def fly(self):
        """
        Print that the bird is flying.
        """
        print("The bird is flying")
    
    def habitat(self):
        """
        Print the bird's habitat.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A flying fish that inherits from both Fish and Bird.
    Demonstrates multiple inheritance.
    """
    
    def swim(self):
        """
        Override the swim method from Fish.
        """
        print("The flying fish is swimming!")
    
    def fly(self):
        """
        Override the fly method from Bird.
        """
        print("The flying fish is soaring!")
    
    def habitat(self):
        """
        Override the habitat method.
        FlyingFish has access to both habitats.
        """
        print("The flying fish lives both in water and the sky!")
