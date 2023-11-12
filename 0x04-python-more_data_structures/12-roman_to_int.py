#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None:
        return 0
    
    frst_num = 0
    scnd_num = 0
    
    for num in roman_string:
        if num == 'I':
            v = 1
        elif num == 'V':
            v = 5
        elif num == 'X':
            v = 10
        elif num == 'L':
           v = 50
        elif num == 'C':
            v = 100
        elif num == 'D':
            v = 500
        elif num =='M':
            v = 1000
        else:
            return 0

        if v > scnd_num:
            frst_num += v - scnd_num * 2
        else:
            frst_num += v
        
        scnd_num = v
        
    return frst_num4
