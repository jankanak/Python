import re
pp=input()
for i in re.split("[,\<]?",pp):
    print(i)