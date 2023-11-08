#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    notcom = []
    for i in set_1:
        if i not in set_2:
            notcom.append(i)
    for i in set_2:
        if i not in set_1:
            notcom.append(i)

    return notcom
