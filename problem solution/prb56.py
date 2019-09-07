import json

d={"empolyees":[{"firstname":"kanak","lastname":"hassan"},
{"dept":"cse","university":"pust"}]}

with open ('kanak.json','w') as file:
    json.dump(d,file,indent=4,sort_keys=True)