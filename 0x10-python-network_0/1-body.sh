#!/bin/bash
# takes in a url, sends a GET request to the url, displays the body of the respons
curl -sGf "$1"
