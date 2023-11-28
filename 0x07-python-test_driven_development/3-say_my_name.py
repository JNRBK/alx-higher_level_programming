#!/usr/bin/python3
"""function for printing a name"""


def say_my_name(first_name, last_name=""):
    """say_my_name

    Args:
    @first_name: 1st parameter
    @last_name: 2nd parameter by default set for ""

    Return:
    first and last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
