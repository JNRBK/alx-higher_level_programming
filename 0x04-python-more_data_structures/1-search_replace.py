#!/usr/bin/python3
def search_replace(my_list, search, replace):
    repl = []
    for newnum in my_list:
        if newnum == search:
            repl.append(replace)
        else:
            repl.append(newnum)
    return repl
