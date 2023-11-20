#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        itr = 0
        for n in range(x):
            print(my_list[n], end="")
            itr += 1
    except IndexError:
        pass
    finally:
        print()
    return itr
