#!/usr/bin/python3
"""
class base geometry
"""


class BaseGeometry:
    """structure of class"""
    def area(self):
        """ area function that raises and exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator that validates value
        Args:
        @name: string representing name
        @value: value of name
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
