#!/usr/bin/python3
"""Function to return the list of available
   attributes and methods of an object:
   """


def lookup(obj):
    """
    Args:
    @obj: object for attribute
    Return: List of all available attributes
    """
    return dir(obj)
