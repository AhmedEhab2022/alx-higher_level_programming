#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, sends a request to that URL, and displays the size of the body of the response
curl -s -I -H 'Content-Length' "$1"
