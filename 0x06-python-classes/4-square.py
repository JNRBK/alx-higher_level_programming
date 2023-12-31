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

    '''property of def size to retrieve it'''
    @property
    def size(self):
        return self.__size

    '''property setter to set it'''
    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''calculate and return area of square'''
        return self.__size ** 2
