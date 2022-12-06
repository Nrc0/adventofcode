path='input\\day06.txt'

with open(path) as f:
    data = f.read().strip()

p = data
i = 0; j = 0

# part 1
while len(set(p[:4])) != 4:
    p = p[1:]
    i += 1

#part 2
while len(set(p[:14])) != 14:
    p = p[1:]
    j += 1

print(i+4)
print(j+14)
