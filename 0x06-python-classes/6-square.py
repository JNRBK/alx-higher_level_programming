#!/usr/bin/python3
'''Square Class with the size'''


class Square:
    """ __init__ method.
    size: size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
        self.position = value
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(x, int) or x > 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''calculate and return area of square'''
        return self.__size ** 2

    """
    my_print print a square shape to stdout with
    the character "#"
    """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print('#', end="")
                print()
