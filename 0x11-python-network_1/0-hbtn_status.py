#!/usr/bin/python3

# Import the 'urllib.request' module
import urllib.request

# Define the URL to be fetched
url = 'https://alx-intranet.hbtn.io/status'

# Send a GET request to the URL and store the response in a 'response' object
with urllib.request.urlopen(url) as response:
    # Read the content of the response and store it as a bytes object in the 'content' variable
    content = response.read()
    
    # Decode the content from bytes to UTF-8 and store it as a string in the 'utf8_content' variable
    utf8_content = content.decode('utf-8')

# Print out information about the response
print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
print(f"\t- utf8 content: {utf8_content}")

