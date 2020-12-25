#!/usr/bin/env python
import fileinput

fn="input_test.txt"
#fn="input.txt"

def edges(tile):
    edges = [tile[0], tile[-1]]
    l, r = "", ""
    for row in tile:
        l += row[0]
        r += row[-1]
    
    edges.append(l)
    edges.append(r)
    
    return edges    

def flipped(edge):
    return list(map(lambda e: e[::-1], edge))

dtiles = { tt[0]:tt[1:] for tt in [t.strip().split("\n") for t in open(fn).read().split("\n\n")] }


res = {}
for tile in dtiles:
    comb = edges(dtiles[tile])
    comb += flipped(comb)

    other_edges = [ edges(dtiles[t]) for t in dtiles if t != tile ]
    other_edges = [ item for sublist in other_edges for item in sublist ]

    acc = 0
    for c in comb:
        acc += other_edges.count(c)

    res[tile] = acc

corners = [t for t in res if res[t] == 2]

print(res)

acc = 1
for c in corners:
    acc *= int(c.replace("Tile", "").replace(":", "").strip())
print(f"Corners: {acc}")