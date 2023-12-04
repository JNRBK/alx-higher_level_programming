#!/usr/bin/python3
"""
Function that return true if object is an instance of a class
that inherited from specified class otherwise false
"""


def inherits_from(obj, a_class):
    """
    Args:
    @obj: object for class
    @a_class: class of the object
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
