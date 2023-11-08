#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    list_it = list(new)

    sum_it = 0
    for ind in list_it:
        sum_it += ind
    return sum_it
