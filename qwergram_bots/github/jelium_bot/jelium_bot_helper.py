import requests
import sys

response = requests.get(sys.argv[1])
if response.ok:
    print(response.json())
else:
    print(response.reason)
