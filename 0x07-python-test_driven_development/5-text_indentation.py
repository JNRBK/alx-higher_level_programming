#!/usr/bin/python3
"""
Text indentation module
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after., ? and :
    Args:
    @text: text to indentate

    Returns:
    nothing , new text or raise an error

    """
    if type(text) is not str or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    text = text.strip()
    flag = False
    symbols = ['.', '?', ':']
    for c in text:
        if c == ' ' and flag is True:
            continue
            flag = False
        if c in symbols:
            print(c)
            print()
            flag = True
        else:
            print(c, end="")
            flag = False
