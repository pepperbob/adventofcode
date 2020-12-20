#!/usr/bin/env python
import fileinput
from collections import deque
import operator

directions = { "E": (1, 0), "S": (0, -1), "W": (-1, 0), "N": (0,1) }

def move(ship, op):        
    howfar = int(op[1:])
    currloc = ship["pos"]
    direction = ship["dir"] if op[0] == "F" else op[0]
    addtotal = tuple([howfar*x for x in directions[direction]])
    return {"pos": tuple(map(operator.add, currloc, addtotal)), "dir": ship["dir"]}

def rotate(ship, op):
    dirs = deque(list("ESWN"))
    currentidx = dirs.index(ship["dir"])
    dirs.rotate(currentidx*-1)
    
    lr = -1 if op[0] == "R" else 1
    many = lr * int(int(op[1:])/90)
    dirs.rotate(many)

    return {"pos": ship["pos"], "dir": dirs.popleft()}

ship = { "pos": (0, 0), "dir": "E" }

ops = list(map(lambda  s: s.strip(), fileinput.input()))

for op in ops:
    ship = rotate(ship, op) if op[0] in list("LR") else move(ship, op)
    print(f"{op} => {ship}")

print(f"Manhatten: {sum((abs(ship['pos'][0]), abs(ship['pos'][1])))}")