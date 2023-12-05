#!/usr/bin/python3
"""
BaseGeometry module
"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """ public instance """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public method that validates value
        Args:
        @name: string representing name
        @value: value of name
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Instantiation with width and height
    Args:
    @width: rectangle's
    @height: rectangle's
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ public instance """
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")


""" Square module """


class Square(BaseGeometry):
    """ Instantiation with size
    Args:
    @size: square size
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ area of square """
        return self.__size ** 2

    def __str__(self):
        return (f"[Rectangle] {self.__size}/{self.__size}")
