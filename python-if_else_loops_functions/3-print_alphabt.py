#!/usr/bin/python3
# Yalnız BİR print funksiyası, string format ilə
print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(
    *[chr(i) for i in range(97, 123) if chr(i) not in ['q', 'e']]
), end="")
