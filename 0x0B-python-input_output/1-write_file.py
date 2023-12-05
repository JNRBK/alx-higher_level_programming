#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
returns the number of characters written:
"""


def write_file(filename="", text=""):
    """
    Args:
    @filename: name of file written to
    @text: text written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        write_file = file.write(text)
        return write_file
