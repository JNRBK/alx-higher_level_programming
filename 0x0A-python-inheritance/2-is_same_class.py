#!/usr/bin/python3
"""
function that returns True if
the object is exactly an instance of
specified class otherwise False
"""


def is_same_class(obj, a_class):
    """
    Args:
    @obj: object
    @a_class: class of the object to verify
    Return:
    True if the object is exactly an instance of the class
    otherwise False
    """
    return type(obj) is a_class
