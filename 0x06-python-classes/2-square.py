#!/usr/bin/python3
'''Square Class with the size'''


class Square:
    """ __init__ method.
    size: size of square
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
