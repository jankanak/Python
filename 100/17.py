total_amount=0

while True:
    bank=input ()
    if not bank:
        break
    value=bank.split(' ')
    
    depositorwithdrawal=value[0]
    amount=int(value[1])
    
    if depositorwithdrawal=="D":
        total_amount +=amount
    elif depositorwithdrawal=="W":
        total_amount -=amount
    else:
        pass

print(total_amount)