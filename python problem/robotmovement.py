import math
pos=[0,0]
while True:
    s=input()
    if not s:
        break
    movement=s.split(" ")
    direction=movement[0]
    steps=int(movement[1])
    if direction=='u':
        pos[0]+=steps
    elif direction=='d':
        pos[0]-=steps
    elif direction =='l':
        pos[1]-=steps
    elif direction =='r':
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2 +pos[0]**2))))
