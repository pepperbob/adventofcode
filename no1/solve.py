import itertools

target=2020
res = []

with open("input", "r") as f:
    lines = f.readlines()
lines = [int(l) for l in lines]


cross = itertools.product(lines, lines, lines);

print(cross)

for r in cross:
    if(sum(r)==target):
        print(r[0]*r[1]*r[2])

