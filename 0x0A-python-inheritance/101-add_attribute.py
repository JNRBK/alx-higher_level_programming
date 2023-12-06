#!/usr/bin/python3
"""
function that adds a new attribute to an object
if it's possible
"""


def add_attribute(obj, attr1, attr2):
    """
    Args:
    @attr1: first attribute
    @attr2: second attribute
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr1, attr2)
