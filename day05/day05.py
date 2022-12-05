import string
import sys
from copy import deepcopy

path='input\\day05.txt' # from C:\\

def parse_txt(txt):
    alist = [""]*10
    for line in txt[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != " ": alist[i+1] += box
    return alist
    
data = open(path).read()
a, instruc = [part.split("\n") for part in data.split("\n\n")]
# print("instruc: ",instruc)
alist = parse_txt(a)
# print("alist: ",alist)
p1, p2 = alist[:], alist[:]
for line in instruc:
    _, n, _, src, _, dest = line.split()
    n = int(n); src = int(src); dest = int(dest)

    p1[src], p1[dest] = p1[src][n:],  p1[src][:n][::-1] + p1[dest]
    p2[src], p2[dest] = p2[src][n:],  p2[src][:n]       + p2[dest]
    
# print("p1: ",p1); print("p2: ",p2)
#print first val of each column in list p
print("Part 1:", "".join(s[0] for s in p1 if s))
print("Part 2:", "".join(s[0] for s in p2 if s))
