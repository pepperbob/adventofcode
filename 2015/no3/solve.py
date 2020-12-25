import operator

dirs = {
    "^": (0,1),
    ">": (1,0),
    "<": (-1,0),
    "v": (0,-1)
}

ops = list(open("input.txt").read().strip())

# part 1

curr = (0, 0)
pos = set()
pos.add(curr)
for op in ops:
    curr = tuple(map(operator.add, dirs[op], curr))
    pos.add(curr)

print(f"Total Houses: {len(pos)}")

# part 2:
santa = ops[::2]
robo = ops[1::2]

curr = (0, 0)
pos = set()
pos.add(curr)
for op in santa:
    curr = tuple(map(operator.add, dirs[op], curr))
    pos.add(curr)

curr = (0,0)
for op in robo:
    curr = tuple(map(operator.add, dirs[op], curr))
    pos.add(curr)

print(f"Total Houses with Rob: {len(pos)}")