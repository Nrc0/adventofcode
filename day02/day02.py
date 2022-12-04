import string

path='input\\day2.txt'

with open(path,'r',encoding='utf-8-sig') as f:
    data = f.read().split("\n")
    #print(data)

tab1= {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3,
    "B X": 1,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2,
    "C Z": 3 + 3
}
tab2= {
    "A X": 3,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2,
    "C Y": 3 + 3,
    "C Z": 1 +6
}

res1 = res2 = 0
for i in data:
    res1 += tab1[i]
    res2 += tab2[i]

print("res1: ",res1)
print("res2: ",res2)
