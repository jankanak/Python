import json
from pprint import pprint

with open('kanak.json','r') as file:
    d=json.loads(file.read())

pprint(d)
