#!/usr/bin/env python
import fileinput
import operator
import re

ops = [s for s in list(map(lambda  s: s.strip(), fileinput.input())) if len(s) > 1]

flag = None
ranges = []
tickets = []
types = dict()
myticket = ()
for idx, op in enumerate(ops):
    if(op[0] in list("dacrsptwz")):
        definition = op.split(":")
        types[definition[0]]=idx
        for r in [tuple(r.split("-")) for r in re.findall(r"(\d+\-\d+)", definition[1])]:
            ranges.append((int(r[0]), int(r[1]), definition[0]))
    elif(op[0] in list("y")):
        flag="m"
    elif(op[0] in list("n")):
        flag="t"
    elif(flag == "m"):
        myticket = tuple(map(lambda ss: int(ss), op.split(",")))
    elif(flag == "t"):
        tickets.append(tuple(map(lambda ss: int(ss), op.split(","))))

invalidnumbers = []
valids = []
rangeorder = []
for t in tickets:
    isValid=True
    for n in t:
        hitrange = list(filter(lambda r: r[0]<=n<=r[1], ranges))
        if len(hitrange)==0:
            invalidnumbers.append(n)
            isValid=False

    if(isValid):
        valids.append(t)

print(f"Solutation 1: {sum(invalidnumbers)}")

def findrange(i, ranges):
    hits = list(filter(lambda r: r[0]<=i<=r[1], ranges))
    return [r[2] for r in hits]

from collections import defaultdict

poss = defaultdict(lambda: list(types.keys()))
for v in valids:
    for idx, p in enumerate(v):
        posforp = findrange(p, ranges)

        # intersect
        poss[idx] = list(set(posforp) & set(poss[idx]))


bykeylength = sorted(poss.keys(), key=lambda k: len(poss[k]))

# assume first 1 element, second 2, ...
for idx, a in enumerate(bykeylength):
    for b in bykeylength[idx+1:]:
        poss[b].remove(poss[a][0])

print("\n\n")
sol2 = 1
for k in poss.keys():
    if(poss[k][0].startswith("departure")):
        sol2 *= myticket[k]

print(f"Solution 2: {sol2}")