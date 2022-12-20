import string

path='day03/day03.txt'
p1 = 0
p2 = 0

with open(path,'r',encoding='utf-8-sig') as f:
    data = f.read().split("\n")


# part1
for i in data:
    a = i[:len(i)//2]
    b = i[-len(i)//2:]
    occur= (set(a) & set(b)).pop()
    if occur.islower():
        p1 += ord(occur) - ord("a") + 1
    else:
        p1 += ord(occur) - ord("A") + 27
print ('p1 :',p1)

# part2
for i,j,k in zip(data[::3], data[1::3], data[2::3]):
    badge = (set(i) & set(j) & set(k)).pop() 
    if badge.islower():
        p2 += ord(badge) - ord("a") + 1
    else:
        p2 += ord(badge) - ord("A") + 27
print ('p2 :',p2)
