#!/usr/bin/env python3
"""
Task 0: Abstract Animal Class and its Subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract Animal class.
    This class cannot be instantiated directly because it has
    an abstract method 'sound'.
    """
    
    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.
        
        Returns:
            str: The sound the animal makes
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    Implements the abstract sound() method from Animal.
    """
    
    def sound(self):
        """
        Returns the sound of a dog.
        
        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    Implements the abstract sound() method from Animal.
    """
    
    def sound(self):
        """
        Returns the sound of a cat.
        
        Returns:
            str: "Meow"
        """
        return "Meow"
