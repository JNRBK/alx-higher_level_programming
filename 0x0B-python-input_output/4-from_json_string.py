#!/usr/bin/python3
"""
Function that returns an object py data structure
represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """
    Args:
    @my_str: string to return
    """
    return json.loads(my_str)
