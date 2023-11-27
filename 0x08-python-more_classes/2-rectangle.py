#!/usr/bin/python3
"""define a Rectangle class"""


class Rectangle:
    """rectangle"""

    def __init__(self, width=0, height=0):
        """
        args:
        @width = rectangle width int only
        @height = rectangle height int only
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculating rectangle's parameter"""
        if self.__width == 0 or self.__height == 0:
            self.__perimeter = 0
        return 2 * (self.width + self.__height)
