#!/usr/bin/env python3
"""
Task 5: Dragon with Mixins
"""


class SwimMixin:
    """
    Mixin class that provides swimming capability.
    """
    
    def swim(self):
        """
        Print that the creature swims.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying capability.
    """
    
    def fly(self):
        """
        Print that the creature flies.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class that inherits from both SwimMixin and FlyMixin.
    Demonstrates the use of mixins.
    """
    
    def roar(self):
        """
        Print that the dragon roars.
        """
        print("The dragon roars!")
