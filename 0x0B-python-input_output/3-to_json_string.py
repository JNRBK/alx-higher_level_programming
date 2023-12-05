#!/usr/bin/python3
"""
Function that returns the JSON representation
of an object (String):
"""


import json


def to_json_string(my_obj):
    """
    Args:
    @my_obj: string to return json representation of
    """
    return json.dumps(my_obj)
