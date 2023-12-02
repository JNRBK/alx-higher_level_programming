#!/usr/bin/python3
"""
add integer

int / float only otherwise raise TypeError
casted into integer
"""


def add_integer(a, b=98):
    """
    Args:
    @a = 1st parameter
    @b = 2nd parameter = 98 if no value given

    Return:
    a + b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
