#! /usr/bin/env python

import operator

curr = 0
pos = (0,0)

directions = {
    "R": 90,
    "L": 270
}

movement = {
    0: (1,0),
    90: (0,1),
    180: (-1,0),
    270: (0,-1)
}

trace = []

input = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"

all = [x.strip() for x in input.split(",")]

for a in all:
    x1, x2 = a[0], int(a[1:])
    
    curr = curr + directions[x1]    
    move = tuple([x for x in movement[curr%360]])

    for m in range(x2):
        pos = tuple(map(operator.add, pos, move))
        
        if pos in trace:
            print(f"Been here {pos}")
   
        trace.append(pos)
    
print(pos)
print(sum([abs(x) for x in pos]))
