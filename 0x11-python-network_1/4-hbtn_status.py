#!/usr/bin/python3
"""
python script that fetches url using package requests
"""

import requests

if __name__ == "__main__":
    ftch = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(ftch.text)))
    print("\t- content: {}".format(ftch.text))
