import re
values=[]

item=[x for x in input().split (",")]

for p in item:
    if len(p)<6 and len(p)>12:
        continue
    else:
        pass

    if not re.search("[a-z]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[1-9]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    else:
        pass
    values.append(p)

print(",".join(values))