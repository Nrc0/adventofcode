import string
#import re

path='input\\day4.txt'
p1 = 0
p2 = 0

with open(path,'r',encoding='utf-8-sig') as f:
    data = f.read().split("\n")


#part 1
for i in data:
    a,b=i.split(",")
    a1,a2=map(int,a.split("-"))
    b1,b2=map(int,b.split("-"))
    if a1 <= b1 <= b2 <= a2 or (b1 <= a1 <= a2 <= b2):
        p1 += 1

# part 2
for i in data:
    a,b=i.split(",")
    a1,a2=map(int,a.split("-"))
    b1,b2=map(int,b.split("-"))
    if a2 >= b1 and a1 <= b2 or (b2 > a1 and b1 <= a2):
        p2 += 1

print ('p1 :',p1)
print ('p2 :',p2)
