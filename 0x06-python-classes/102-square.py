#!/usr/bin/python3
'''Square Class with the size'''


class Square:
    """ __init__ method.
    size: size of square
    """
    def __init__(self, size=0):
        self.__size = size

    '''property of def size to retrieve it'''
    @property
    def size(self):
        return self.__size

    '''property setter to set it'''
    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''calculate and return area of square'''
        return self.__size ** 2

    def __eq__(self, other):
        '''handle equal'''
        return self.area() == other.area()

    def __ne__(self, other):
        '''handle not equal'''
        return self.area() != other.area()

    def __ge__(self, other):
        '''handle greater/equal than'''
        return self.area() >= other.area()

    def __le__(self, other):
        '''handle lower/equal than'''
        return self.area() <= other.area()

    def __gt__(self, other):
        '''handle greater than'''
        return self.area() > other.area()

    def __lt__(self, other):
        '''handle lower than'''
        return self.area() < other.area()
