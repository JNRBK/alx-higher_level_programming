#!/bin/bash
#script that takes in a URL as an argument sends a GET request and display body of response
curl -sH "X-School-User-Id: 98" "$1"
