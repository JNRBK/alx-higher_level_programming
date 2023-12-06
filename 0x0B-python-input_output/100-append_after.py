#!/usr/bin/python3
"""
Function that inserts a line of text to a file
after each line containing a specific string/word
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Args:
    @filename: file's name
    @search_string: string/word to search for
    @new_string: new string/word to append to search string
    """
    with open(filename, 'r') as file:
        content = file.readlines()

    new_f = []
    for line in content:
        new_f.append(line)
        if search_string in line:
            new_f.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(new_f)
