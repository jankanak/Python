sentences=input()
check={"Digits":0,"Letters":0}
for c in sentences:
    if c.isdigit():
        check['Digits'] +=1
    elif c.isalpha():
        check['Letters'] +=1
    else:
        pass

print("Numbers of digits" ,check['Digits'])
print("Numbers of Letters" ,check['Letters'])

