#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    total = 0

    ro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for n in range(len(roman_string)):
        if n + 1 < len(roman_string) and \
                ro[roman_string[n]] < ro[roman_string[n + 1]]:
            total -= ro[roman_string[n]]
        else:
            total += ro[roman_string[n]]
    return total
