input_path='input\\day09.txt'

rope = [0] * 10
seen = [set([x]) for x in rope]
dirs = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}
sign = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))

for line in open(input_path):
    d, n = line.split()

    for _ in range(int(n)):
        rope[0] += dirs[d]

        for i in range(1, 10):
            dist = rope[i-1] - rope[i]
            if abs(dist) >= 2:
                rope[i] += sign(dist)
                seen[i].add(rope[i])

print(len(seen[1]), len(seen[9]))