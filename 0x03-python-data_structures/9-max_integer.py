#!/usr/bin/python3
def max_integer(my_list=[]):
    for idx in my_list:
        if idx < 0:
            return None
        my_list.sort()
    return my_list[-1]
