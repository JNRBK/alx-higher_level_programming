#!/usr/bin/python3
"""
function that return True if object is an instance
of or if the object is an instance of a class that
inherited from, otherwise Return False
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
    @obj: object
    @a_class: class of object

    Return: True or False
    """
    return isinstance(obj, a_class)
