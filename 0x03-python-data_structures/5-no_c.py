#!/usr/bin/python3
def no_c(my_string):
    noc = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            noc += char
    return noc
