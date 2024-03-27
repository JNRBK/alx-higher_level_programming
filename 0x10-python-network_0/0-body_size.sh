#!/bin/bash

url="$1"

curl -s "$url" | grep -i 'Content-Length:' | awk '{print $2}'
