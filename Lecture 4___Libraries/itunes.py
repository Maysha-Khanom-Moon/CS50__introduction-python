# sys and json module come with python

# pip install requests
# JSON: used nowadays as a language agnostic format for exchanging data between computer
# agnostic language: we can use any language to read and write json

# .json(): it make a dict format for python


import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit() # program will stop execution
               # return 0 of main function


# https://itunes.apple.com/search?entity=song&limit=1&term=zyan
# python itunes.py weezer
response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])
# print(response.json())

# make it more readable with indentation
# print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])