#!/bin/bash
# sends request to url passed as an argument and displays only status of code 
curl -so /dev/null -w "%{http_code}" "$1"
