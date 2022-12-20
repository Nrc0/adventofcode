import string

path='day01/day01.txt'
cal=[]

with open(path,'r',encoding='utf-8-sig') as f:
    data=f.read().split("\n\n")
    for i in data:
        sum_cal = sum(map(int,i.splitlines()))
        cal.append(sum_cal)

print(max(cal))
cal=sorted(cal)
print(sum(cal[-3:]))
