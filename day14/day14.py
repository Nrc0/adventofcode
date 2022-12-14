import math
from copy import deepcopy
from collections import defaultdict, deque

input_path ='C:\\...\\input\\day14.txt'

data = open(input_path).read().strip()
lines = [x for x in data.split('\n')]

R = set()
for line in lines:
    previous = None
    for pt in line.split('->'):
        x,y = pt.split(',')
        x,y = int(x),int(y)
        if previous is not None:
            dx = x-previous[0]
            dy = y-previous[1]
            len_ = max(abs(dx),abs(dy))
            for i in range(len_+1):
                xx = previous[0]+i*(1 if dx>0 else (-1 if dx<0 else 0))
                yy = previous[1]+i*(1 if dy>0 else (-1 if dy<0 else 0))
                R.add((xx,yy))
        previous = (x,y)

floor = 2+max(r[1] for r in R)
#print(floor)
low_x = min(r[0] for r in R)-2000
hight_x = max(r[0] for r in R)+2000
for x in range(low_x, hight_x):
    R.add((x,floor))

p1_done = False
for t in range(1000000):
    rock = (500,0)
    while True:
        if rock[1]+1>=floor and (not p1_done):
            p1_done = True
            print(t)
        if (rock[0],rock[1]+1) not in R:
            rock = (rock[0],rock[1]+1)
        elif (rock[0]-1,rock[1]+1) not in R:
            rock = (rock[0]-1, rock[1]+1)
        elif (rock[0]+1, rock[1]+1) not in R:
            rock = (rock[0]+1, rock[1]+1)
        else:
            break
    if rock == (500,0):
        print(t+1)
        break
    R.add(rock)
