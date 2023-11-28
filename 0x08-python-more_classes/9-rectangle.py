#!/usr/bin/python3
"""define a Rectangle class"""


class Rectangle:
    """rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        args:
        @width = rectangle width int only
        @height = rectangle height int only
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """calculating rectangle's parameter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.width + self.__height)

    def __str__(self):
        """ rectangle __str__"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for i in range(self.height):
            rectangle += str(self.print_symbol) * self.width
            if i < (self.height - 1):
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        """rectangle __repr__"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """deletes an instance of a Rectangle"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Bigger or equal: parameters must be an instance of a rectangle
        return rect 1 if both areas are equal other wise return
        rect_2
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method of a square
        return width == height == size
        """
        return cls(size, size)
