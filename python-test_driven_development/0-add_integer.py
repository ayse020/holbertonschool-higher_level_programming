#!/usr/bin/python3
"""
0-add_integer modulu
İki tam ədədin toplanması üçün funksiya
"""


def add_integer(a, b=98):
    """
    İki ədədi toplayır və tam ədəd qaytarır
    
    Args:
        a: birinci ədəd (tam və ya kəsr)
        b: ikinci ədəd (tam və ya kəsr), default 98
    
    Returns:
        a və b-nin toplamı (tam ədəd)
    
    Raises:
        TypeError: a və ya b tam/kəsr ədəd deyilsə
    """
    
    # a-nın tipini yoxlamaq
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    
    # b-nin tipini yoxlamaq
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    
    # Əgər float-dursa, int-ə çevirmək
    a = int(a)
    b = int(b)
    
    # Toplama və nəticəni qaytarma
    return a + b
