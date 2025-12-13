#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Siyahıdan müəyyən sayda element çap edir.
    
    Args:
        my_list: Çap ediləcək elementləri ehtiva edən siyahı
        x: Çap ediləcək elementlərin sayı
    
    Returns:
        Həqiqətən çap edilən elementlərin sayı
    """
    count = 0  # Çap edilən elementlərin sayını saxlayırıq
    
    try:
        # 0-dan x-1-ə qədər olan indekslər üçün dövr edirik
        for i in range(x):
            # Siyahının i-ci elementinə çatmağa çalışırıq
            print(my_list[i], end="")
            count += 1  # Uğurla çap etdik, sayı artırırıq
    except IndexError:
        # Siyahıda i-ci element yoxdursa, xətanı gözləyirik
        # Bu halda sadəcə dövrü dayandırırıq
        pass
    finally:
        # Bütün çap edilənlərdən sonra yeni sətirə keçirik
        print()
    
    return count
