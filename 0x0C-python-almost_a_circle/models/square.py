#!/usr/bin/python3
""" class module (Square) """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
        @size: size of square
        @x: coordinate
        @y: coordinate
        @id: identity of class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """property getter"""
        return self.width

    @size.setter
    def size(self, value):
        """property setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation __str__"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """update arguments wth attributes"""
        try:
            if args:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            for keys, values in kwargs.items():
                setattr(self, keys, values)
        except Exception:
            pass

    def to_dictionary(self):
        """
        returns the dictionary representation
        of the square
        """
        diction = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return diction
