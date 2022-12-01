import string

path='input\\day1.txt'
cal=[]

with open(path,'r',encoding='utf-8-sig') as f:
    data=f.read().split("\n\n")
    for i in data:
        sum_cal = sum(map(int,i.splitlines()))
        cal.append(sum_cal)

print(max(cal))
