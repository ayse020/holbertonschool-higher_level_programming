#!/usr/bin/python3
""" Roman to Integer test file """
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "III"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LVIII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "MCMXCIV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
