#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    """
    Args:
    @value: value of class
    """
    def __init__(self, value):
        self.__value = value

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
