#!/usr/bin/python3
"""
Function that returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """
    Args:
    @obj: instance of a class
    """
    return vars(obj)
