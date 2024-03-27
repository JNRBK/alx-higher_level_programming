#!/bin/bash
# takes in a URl and displays all HTTP methods the server will accept
curl -sI "$1"| awk '/Allow:/ {print $2, $3, $4}'
