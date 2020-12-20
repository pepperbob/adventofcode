#!/usr/bin/env python
import fileinput
from collections import deque
from itertools import count
from math import gcd

# kleinste gemeinsame vielfache
def lcm(a, b):
    # a*b geteilt durch größten gemeinsame teiler von a und b
	return a * b // gcd(a, b)

# https://github.com/mebeim/aoc/blob/master/2020/solutions/day13.py

ops = list(map(lambda  s: s.strip(), fileinput.input()))
raw = ops[1].split(",")

busses = []
for idx, b in filter(lambda v: v[1] != "x", enumerate(raw)):
    busses.append((idx, int(b)))

time, step = busses[0]
for delta, period in busses[1:]:
    for time in count(time, step):
        if(time+delta) % period == 0:
            print(f"Bus {period} found")
            break
    step = lcm(step, period)

print(f"Answer: {time}")