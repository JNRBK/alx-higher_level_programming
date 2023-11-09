#!/usr/bin/python3
def weight_average(my_list=[]):
    sums = 0
    adds = 0
    if not my_list:
        return 0
    for num in my_list:
        sums += num[0] * num[1]
        adds += num[1]
    if adds == 0:
        return 0
    avg = sums / adds

    return avg
