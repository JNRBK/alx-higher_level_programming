#!/usr/bin/python3
"""
python script takes url , send request to url and
display value of X-Request-id variable
"""
import urllib.request
from sys import argv

with urllib.request.urlopen(argv[1]) as var:
    print(var.headers.get('X-Request-id'))
