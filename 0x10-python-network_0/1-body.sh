#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}" $1 | grep 200 >/dev/null && curl -s $1
