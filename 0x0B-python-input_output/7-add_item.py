#!/usr/bin/python3
"""
script that adds all arguments to a python list
and then save them to a file
"""

import sys


save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file


try:
    load = load_from("add_item.json")
except FileNotFoundError:
    load = []

for arguments in sys.argv[1:]:
    load.append(arguments + '\n')

save_to(load, "add_item.json")
