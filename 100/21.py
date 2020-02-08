# A robot moves in a plane starting from the original point (0,0). 
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following:
# a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

import math
position=[0,0]

while True:
    s=input()
    if not s:
        break
    robot=s.split(" ")
    movement=robot[0]
    steps=int(robot[1])

    if movement=="UP":
        position[0] +=steps
    elif movement=="DOWN":
        position[0]-=steps
    elif movement =="LEFT":
        position[1] -=steps
    elif movement =="RIGHT":
        position[1] +=steps
    else:
        pass

print(round(math.sqrt(position[0]**2+position[1]**2)))
