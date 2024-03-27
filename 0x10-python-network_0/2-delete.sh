#!/bin/bash
# Sends a DELETE request to the url passed as the first argument and displays the body of response
curl -sX DELETE "$1"
