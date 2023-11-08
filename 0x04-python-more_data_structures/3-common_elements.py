#!/usr/bin/python3
def common_elements(set_1, set_2):
    com = []
    for e in set_1:
        if e not in set_2:
            exit
        else:
            com.append(e)
    print(com)
