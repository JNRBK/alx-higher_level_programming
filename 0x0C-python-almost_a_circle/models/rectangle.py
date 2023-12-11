#!/usr/bin/python3
""" Class Rectangle (inherited) from Base class"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Args:
        @width: rectangle's width
        @height: rectangle's height
        @x = coordinate
        @y = coordinate
        @id = identity
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """property getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter for height"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """property getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter for x"""
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """property getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter for y"""
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """ function to calculate area of rectangle """
        return (self.__width * self.__height)

    def display(self):
        """ prints in stdout the Rectangle's instance with-#-
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        string represent the rectangle
        [Rectangle] (id) x/y - width/height
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y,
                        self.width, self.height))

    def update(self, *args, **kwargs):
        """ public method that assigns an argument
        to each attribute """
        try:
            if args:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            for keys, values in kwargs.items():
                setattr(self, keys, values)
        except Exception:
            pass

    def to_dictionary(self):
        """
        public method that returns the dictionary
        representation of a Rectangle
        """
        diction = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return diction
