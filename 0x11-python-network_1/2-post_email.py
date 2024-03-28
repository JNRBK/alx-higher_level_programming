#!/usr/bin/python3
"""
script takes in url and an email
sends a post request to the passed url with email as parameter
displays the body of the response decoded in utf-8
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    email = urllib.parse.urlencode({'email': argv[2]}).encode('utf-8')
    Post = urllib.request.Request(argv[1], data=email, method='POST')

    with urllib.request.urlopen(Post) as response:
        print(response.read().decode('utf-8'))
