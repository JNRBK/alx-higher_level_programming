#!/usr/bin/python3
"""
takes url and sends a request to the url ,
displays the value of the variable X-Request-id
in the response header
"""

import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if 'X-Request-Id' in req.headers:
        fetch = req.headers['X-Request-Id']
        print(fetch)
