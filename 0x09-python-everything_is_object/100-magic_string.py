#!/usr/bin/python3
def magic_string():
    """magic_string
    Write a class LockedClass with no class or object attribute, that prevents the user 
    from dynamically creating new instance attributes,
    except if the new instance attribute
    is called first_name.
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
