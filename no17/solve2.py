#!/usr/bin/env python
import fileinput

def findneighbour(cube):
    neighbors = [
        (cube[0]+a, cube[1]+b, cube[2]+c, cube[3]+d) 
        for a in range(-1, 2)
        for b in range(-1, 2)
        for c in range(-1, 2)
        for d in range(-1, 2)
        if not (a,b,c,d)==(0,0,0,0)]

    return neighbors

def countActiveNeighbors(cube, pcubes):
    return len([n for n in findneighbour(cube) if pcubes.get(n) == "#"])

def simulate(pcubes):
    new_pcube = {}
    for c in pcubes:
        active = countActiveNeighbors(c, pcubes)
        if pcubes[c] == "#":
            if active == 2 or active == 3:
                new_pcube[c]="#"
            else:
                new_pcube[c]="."
            
            for n in findneighbour(c):
                if n not in pcubes:
                    if countActiveNeighbors(n, pcubes) == 3:
                        new_pcube[n] = "#"
        else:
            if active == 3:
                new_pcube[c] = "#"
            else:
                new_pcube[c] = "."

    return new_pcube;

ops = [list(s) for s in list(map(lambda  s: s.strip(), fileinput.input())) if len(s) > 1]
pocketcube = {(i, j, 0, 0):ops[i][j] 
             for i in range(len(ops)) 
             for j in range(len(ops[0]))}

for i in range(6):
    pocketcube = simulate(pocketcube)
    print(f"Round {i}\n{pocketcube}")


print(f"Solution 2: {list(pocketcube.values()).count('#')}")
