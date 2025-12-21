#!/usr/bin/python3
"""
0-add_integer modulu
Iki tam ededi toplayan funksiyani temin edir
Bu modul TDD (Test Driven Development) prinsipleri ile yaradilib.
"""


def add_integer(a, b=98):
    """
    Iki tam ededi toplayir.
    
    Args:
        a: Birinci eded (integer ve ya float)
        b: Ikinci eded (integer ve ya float), default deyeri 98
    
    Returns:
        a ve b-nin cemi (integer)
    
    Raises:
        TypeError: Eger a ve ya b integer ve ya float deyilse
    
    Numuneler:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    
    # a-nin tipini yoxlayaq
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # b-nin tipini yoxlayaq
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Eger float-dirsa, integer-e cevirek
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    # Toplama emeliyyatini yerine yetirek
    return a + b
