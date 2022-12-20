input_path ='day15/day15.txt'

from re import compile

data = ''

with open(input_path) as file:
	data = file.read()

target_row = 2000000
ranges = list()

data = list()

coords = compile(r'''Sensor at x\=(-?[0-9]+)\, y\=(-?[0-9]+)\: closest beacon is at x\=(-?[0-9]+)\, y\=(-?[0-9]+)''').finditer
for match in coords(data):
	sx = int(match[1])
	sy = int(match[2])
	bx = int(match[3])
	by = int(match[4])
	
	data.append((sx, sy, bx, by, ))
	
	L1 = abs(sx - bx) + abs(sy - by)
	
	if (sy - L1) <= target_row <= (sy + L1):
		width = L1 - abs(sy - target_row)
		ranges.append((sx - width, sx + width, ))

ranges.sort()

count = 0
head = ranges[0][0]
for x, y in ranges:
	if head < x:
		count += y - x +1
		head = y
	else:
		if head < y:
			count += y - head
			head = y

def heck():
	for target_row in range(0, 4000000):
		ranges = list()
		
		for sx, sy, bx, by in data:
			L1 = abs(sx - bx) + abs(sy - by)
			
			if (sy - L1) <= target_row <= (sy + L1):
				width = L1 - abs(sy - target_row)
				ranges.append((sx - width, sx + width, ))
		
		ranges.sort()
		
		head = ranges[0][0]
		for x, y in ranges:
			if head+1 < x:
				return target_row+4000000*(head+1)
			else:
				if head < y:
					head = y

print(count)
print(heck())
