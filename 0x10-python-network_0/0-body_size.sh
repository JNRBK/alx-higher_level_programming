#!/bin/bash
# takes URL, Sends a request to that url and display size of body

curl -sI "$1" | grep -i 'Content-Length:' | awk '{print $2}'

