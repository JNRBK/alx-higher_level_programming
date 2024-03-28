#!/bin/bash
# sends a JSON post request to a url passed as the first argument, must send post and request contents of a file
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
