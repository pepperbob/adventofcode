#!/usr/bin/env python
import fileinput
from collections import deque

#fn="input_test.txt"
#fn="input.txt"
input = "562893147"
#input = "123456789"

all_cups = list(map(lambda x: int(x), list(input))) + list(range(10, 10000))
start = all_cups[0]

def rotate(cups, label):
    cups = deque(cups)

    while cups[0] != label:
        cups.rotate()

    return list(cups)

input = list(all_cups)

## start the thing:

for y in range(100000):
    current = input[0]

    print(f"Round {y+1}")    
    #print(f"Start {input}")
    #print(f"Current: {current}")

    # pick 3 cups after current
    pickup = [input.pop(1) for x in range(1, 4)]

    #print(f"Pick: {pickup}")

    destination_cup = None
    newlabel = current
    # select new label
    while destination_cup is None:
        newlabel = newlabel - 1

        if(newlabel in pickup):
            continue
        elif newlabel < min(all_cups):
            newlabel = max(all_cups)+1
        else:
            destination_cup = newlabel

    for x in reversed(pickup):
        input.insert(input.index(destination_cup)+1, x)

    #print(f"new current {input[1]}")
    input = rotate(input, input[1])
    
    #print(input)
    #print("")

res = list(map(lambda i: str(i), rotate(input, 1)))
print(" ".join(res[1:3]))