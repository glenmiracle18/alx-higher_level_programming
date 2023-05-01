#!/bin/bash

# Check if an argument was provided
if [ -z "$1" ]
  then
    echo "Please provide a URL as an argument"
    exit 1
fi

# Send a request to the URL and store the response body in a variable
response=$(curl -s -w "%{size_download}" -o /dev/null $1)

# Display the size of the response body in bytes
echo "Size of response body: $response bytes"

