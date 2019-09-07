import json
from pprint import pprint
with open('kanak.json','r+') as file:
    p=json.loads(file.read())
    p["empolyees"].append(dict(first='hello',last='world'))
    file.seek(0)
    json.dump(p,file,indent=4,sort_keys=True)
    file.truncate()


