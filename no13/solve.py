#!/usr/bin/env python
import fileinput
from collections import deque
import operator

ops = list(map(lambda  s: s.strip(), fileinput.input()))

earliest = int(ops[0])
busses = [int(i) for i in ops[1].split(",") if i != "x"]

print(busses)

times = dict()
for b in busses:
    start = 0
    times[b] = []
    curr = start
    while(curr <= earliest):
        curr += b
    times[b] = curr

print(f"my time {earliest}")
for key in sorted(times, key = lambda k: times[k]):
    sol = key * (times[key]-earliest)
    print(f"{key} => wait {times[key]-earliest}")
    print(f"Solution {sol}")
    break