#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in range(len(my_list)):
        num = len(my_list) - 1
        print("{:d}".format(my_list[num]))
        my_list[num] -= 1
