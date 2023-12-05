#!/usr/bin/python3
"""
Function that writes an object to a text file
using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
    @my_obj: object to be written to a text file
    @filename: name of file
    """
    with open(filename, 'w', encoding='utf8') as file:
        jsn = json.dumps(my_obj)
        file.write(jsn)
