#!/usr/bin/env python3
"""Dragon with Mixins"""

class SwimMixin:
    """Mixin for swimming capability"""
    
    def swim(self):
        """Return swimming message"""
        return "The creature swims!"

class FlyMixin:
    """Mixin for flying capability"""
    
    def fly(self):
        """Return flying message"""
        return "The creature flies!"

class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swimming and flying capabilities"""
    
    def roar(self):
        """Dragon's roar"""
        return "The dragon roars!"
    
    def breath_fire(self):
        """Dragon's fire breath"""
        return "The dragon breathes fire!"
