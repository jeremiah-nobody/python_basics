import requests
import json
import sys

if len(sys.argv) != 2:
     sys.exit()

responce = requests.get(f"https://itunes.apple.com/search?entity=song&limit=20&term={sys.argv[1]}")

#responce = requests.get(f"https://google.com/search?q={sys.argv[1]}")

object = responce.json()

for result in object["results"]:
     print(result["trackName"])

#print(json.dumps(responce.json(), indent=2))