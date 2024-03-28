#!/usr/bin/python3
"""
takes url and sends a request to the url ,
displays the value of the variable X-Request-id
in the response header
"""

import requests
from sys import argv

if __name__ == "__main__":
    var = requests.get(argv[1], timeout=5)
    print(var.headers.get('X-Request-Id'))
