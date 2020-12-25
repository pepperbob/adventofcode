#!/usr/bin/env python
import fileinput
import operator
from collections import defaultdict

directions = {
    "w": (0,2),
    "nw": (1,1),
    "ne": (1,-1),
    "e": (0,-2),
    "se": (-1,-1),
    "sw": (-1,1)
}

def neighbors(tile):
    return [tuple(map(operator.add, tile, directions[d])) for d in directions]

rawops = list(map(lambda x: x.strip(), fileinput.input()))

ops = []

for ro in rawops:
    more = False
    op = []
    last = ""
    for curr in ro:
        if more:
            op.append(last + curr)
            more = False
        elif curr == "n" or curr == "s":
            last = curr
            more = True
        else:
            op.append(curr)

    ops.append(op)

known_tiles = defaultdict(lambda: "w")
black = []
for path in ops:
    fin = (0,0)
    for p in path:    
        fin = tuple(map(operator.add, fin, directions[p]))
    
    if known_tiles[fin] == "b":
        known_tiles[fin] = "w"
    else:
        known_tiles[fin] = "b"

print(f"Initial Black Tiles:")
print(len([d for d in known_tiles if known_tiles[d] == "b"]))

# part 2
# init Next-Day
for d in known_tiles.copy():
    for x in neighbors(d):
        if x not in known_tiles:
            known_tiles[x] = "w"

for i in range(100):

    curr_tiles = known_tiles.copy()
    flips = dict()
    for d in curr_tiles:
        all_neighbors = [known_tiles[d] for d in neighbors(d)]
        neighbors_b = len([d for d in all_neighbors if d == "b"])

        if known_tiles[d] == "b" and (neighbors_b == 0 or neighbors_b > 2):
            flips[d] = "w"
        elif known_tiles[d] == "w" and neighbors_b == 2:
            flips[d] = "b"
    
    for x in flips:
        known_tiles[x] = flips[x] 

    print(f"Day {i+1}")

print(len([d for d in known_tiles if known_tiles[d] == "b"]))
print("")