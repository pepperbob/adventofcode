#!/usr/bin/env python
import fileinput
from collections import deque
import operator

directions = { "E": (1, 0), "S": (0, -1), "W": (-1, 0), "N": (0,1) }

def move(ship, op):        
    howfar = int(op[1:])
    currloc = ship["pos"]
    addtotal = tuple([howfar*x for x in ship["waypoint"]])
    return {"pos": tuple(map(operator.add, currloc, addtotal)), "dir": ship["dir"], "waypoint": ship["waypoint"]}

def movewp(ship, op):
    howfar = int(op[1:])
    currloc = ship["waypoint"]
    direction = op[0]
    addtotal = tuple([howfar*x for x in directions[direction]])
    return {"pos": ship["pos"], "dir": ship["dir"], "waypoint": tuple(map(operator.add, currloc, addtotal))}

def rotate(ship, op):
    # rotate waypoint now 
    lr = (1, -1) if op[0] == "R" else (-1, 1)
    many = int(int(op[1:])/90)
    wp = ship["waypoint"]
    for i in range(many):
        wp = tuple(map(operator.mul, lr, reversed(wp)))

    return {"pos": ship["pos"], "dir": ship["dir"], "waypoint": wp}

ship = { "pos": (0, 0), "dir": "E", "waypoint": (10, 1) }

ops = list(map(lambda  s: s.strip(), fileinput.input()))

for op in ops:
    if(op[0] in list("LR")):
        ship = rotate(ship, op)
        pass
    elif(op[0] in list("ESWN")):
        ship = movewp(ship, op)
        pass
    elif(op[0] in list("F")):
        ship = move(ship, op)
    else:
        raise f"NoOp {op}"

    print(f"{op} => {ship}")

print(f"Manhatten: {sum((abs(ship['pos'][0]), abs(ship['pos'][1])))}")