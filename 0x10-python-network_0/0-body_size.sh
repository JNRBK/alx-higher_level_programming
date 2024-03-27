#!/bin/bash
# takes URL, Sends a request to that url and display size of body

curl -sI "$1" | awk '/Content-Length:/ {print $2}'

