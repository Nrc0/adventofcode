import collections

p1=0; p2=0; path = ""
sysfile = collections.defaultdict(int)
input_path='input\\day07.txt'

for line in open(input_path).readlines()[1:]:
    if '..' in line:
        path = path[:path.rindex('/')]
    elif '$ cd' in line:
        path = path + '/' + line[5:]
    elif line.split(' ')[0].isnumeric():
        current = path
        sysfile[""] += int(line.split(' ')[0])
        while current:
            sysfile[current] += int(line.split(' ')[0])
            current = current[:current.rindex('/')] if '/' in current else ""

p1 = sum([v for v in sysfile.values() if v <= 100000])
minimumtofree = sysfile[""] + 30000000 - 70000000
p2= [x for x in sorted(sysfile.values()) if x - minimumtofree > 0][0]
print("p1: ",p1)
print("p2: ",p2)
