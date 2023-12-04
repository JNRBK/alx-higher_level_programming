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
