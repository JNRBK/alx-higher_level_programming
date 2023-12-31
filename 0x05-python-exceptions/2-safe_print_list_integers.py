#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        itr = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                itr += 1
    except (IndexError, ValueError):
        raise

    print()
    return itr
