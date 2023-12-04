#!/usr/bin/python3
""" class MyList that inherits from list """


class MyList(list):
    """
    function print_sorted that prints a list
    in sorted order
    """

    def print_sorted(self):
        print(sorted(self))
