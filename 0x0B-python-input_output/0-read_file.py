#!/usr/bin/python3
"""
Function that reads a text file (UTF-8)
and prints it to stdout:
"""


def read_file(filename=""):
    """
    Args:
    @filename: file to open and read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
