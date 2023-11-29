#!/usr/bin/python3
def copy_list(cpl):
    return cpl[:] if isinstance(cpl, list) else None
