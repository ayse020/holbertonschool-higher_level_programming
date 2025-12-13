#!/usr/bin/python3

def safe_print_integer(value):
    """
    Təhlükəsiz şəkildə tam ədəd çap edir.
    
    Args:
        value: Çap ediləcək dəyər
    
    Returns:
        bool: Dəyər tam ədəddirsə True, əks halda False
    """
    try:
        # value-nun tam ədəd olub olmadığını yoxlamaq üçün format etməyə çalışırıq
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Əgər value tam ədəd deyilsə, xətanı tuturuq və False qaytarırıq
        return False
