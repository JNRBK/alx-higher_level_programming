#!/usr/bin/python3
"""
Function that appends a string at the end of a text
file (utf8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """
    Args:
    @filename: name of file to append to
    @text: text added at the end of file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        append_write = file.write(text)
        return append_write
