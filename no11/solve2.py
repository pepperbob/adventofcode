#!/usr/bin/env python
import fileinput
from collections import defaultdict
import operator

def printseats(seats):
    for s in seats:
        print(s)
    print("\n\n")

directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

seats = list(map(lambda  s: list(s.strip()), fileinput.input()))

print("Setup...")

avail = []
for idxa, a in enumerate(seats):
    for idxb, b in enumerate(a):
        avail.append((idxa,idxb))

adjcellpos = {}
for idxa, a in enumerate(seats):
    for idxb, b in enumerate(a):
        adjcellpos[(idxa, idxb)]= []
        for d in directions:
            # first move in direction:
            r = tuple(map(operator.add, (idxa, idxb), d))
            while(r in avail and seats[r[0]][r[1]] == "."):
                r = tuple(map(operator.add, r, d))
            
            if(r in avail):
                adjcellpos[(idxa, idxb)].append(r)

print("Part Two:")
occupationsafter = [0]
while(True):
    newseats = []
    for idxa, a in enumerate(seats):
        currrow = []
        newseats.append(currrow)
        for idxb, curr in enumerate(a):
            currxy = (idxa, idxb)

            adj = [seats[i[0]][i[1]] for i in adjcellpos[currxy]]
            if(curr == "L"):
                if(sum([i == "#" for i in adj]) == 0):
                    currrow.append("#")
                else:
                    currrow.append(curr)
            elif (curr == "#"):
                if(sum([i == "#" for i in adj]) > 4):
                    currrow.append("L")
                else:  
                    currrow.append(curr)
            else:
                currrow.append(curr)
    
    seats = list(newseats)
    occupied = sum([i == "#" for i in [item for sub in seats for item in sub]])
    
    if(occupied == occupationsafter[-1]):
        print(f"Not Moving after Round {len(occupationsafter)}")
        break

    occupationsafter.append(occupied)
    print(f"Now Occupied: {occupied}")
