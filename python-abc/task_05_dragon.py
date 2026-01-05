#!/usr/bin/env python3
"""Dragon sinifi - Mixin nümunəsi"""


class SwimMixin:
    """Üzmək qabiliyyəti təmin edən mixin"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Uçmaq qabiliyyəti təmin edən mixin"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Həm üzə bilən, həm də uça bilən əjdaha"""
    def roar(self):
        print("The dragon roars!")
