#!/usr/bin/python3
"""
Function that creates an object from a JSON FILE
"""
import json


def load_from_json_file(filename):
    """
    Args:
    @filename: file to create an object from
    """
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
