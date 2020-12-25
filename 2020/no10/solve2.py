#!/usr/bin/env python

import fileinput
from collections import defaultdict

adapters = [0] + sorted(map(int, fileinput.input()))
adapters.append(adapters[-1] + 3)

diffs = defaultdict(int)
counts = defaultdict(int, {0: 1})

print(diffs)
print(counts)

for a, b in zip(adapters[1:], adapters):
    print(f"a,b={a},{b}")
    diffs[a - b] += 1
    # number of ways to reach i'th adapter from previous three possible ones
    print(f"counts= {counts[a - 1]}")
    counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]

print(diffs[1] * diffs[3])
print(counts[adapters[-1]])