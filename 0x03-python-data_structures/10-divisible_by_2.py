#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    of2 = []
    for idx in my_list:
        if idx % 2 == 0:
            of2.append(True)
        else:
            of2.append(False)
    return of2
