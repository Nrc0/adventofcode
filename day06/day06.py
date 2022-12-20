path='day06/day06.txt'

with open(path) as f:
    data = f.read().strip()

i = 0; j = 0

# part 1
while len(set(data[:4])) != 4:
    data = data[1:]
    i += 1

#part 2
while len(set(data[:14])) != 14:
    data = data[1:]
    j += 1

print(i+4)
print(j+14)
