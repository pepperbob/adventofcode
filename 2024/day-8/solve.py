from itertools import combinations, count
from collections import defaultdict

class Point(object):
    def __init__(self, x: int, y: int):
        self.p = (x, y)

    def __add__(self, other):
        return Point(self.p[0] + other.p[0], self.p[1] + other.p[1])

    def __sub__(self, other):
        return Point(self.p[0] - other.p[0], self.p[1] - other.p[1])

    def __repr__(self):
        return f"{self.p}"
    
    def __eq__(self, other):
        return self.p == other.p

    def __hash__(self):
        return hash(self.p)

    def __mul__(self, other):
        return Point(self.p[0]*other, self.p[1]*other)

    def within(self, min, max):
        xmin, ymin = min 
        xmax, ymax = max
        return self.p[0] >= xmin and self.p[1] >= ymin and self.p[0] <= xmax and self.p[1] <= ymax


the_map = open("input").read().splitlines()
upper_bound = (len(the_map)-1, len(the_map[0])-1)
antennas = defaultdict(list) 
for xi, x in enumerate(the_map):
    for yi, y in enumerate(x):
        if y != ".":
            antennas[y].append(Point(xi, yi))

### solution 1
antinodes = set() 
for k in antennas.keys():
    for (a, b) in combinations(antennas[k], 2):
        antinodes.add(a+(a-b))
        antinodes.add(b+(b-a))

unique_freqs = [f for f in antinodes if f.within((0,0), upper_bound)]
print("Solution 1:", len(unique_freqs))

### solution 2:
antinodes = set()
for k in antennas.keys():
    for (a, b) in combinations(antennas[k], 2):
        dist_ab = a-b
        for (anti_a, anti_b) in map(lambda x: (a+(dist_ab*x), b+(dist_ab*x*-1)), count()): 
            a_good = anti_a.within((0,0), upper_bound)
            b_good = anti_b.within((0,0), upper_bound)

            antinodes.add(anti_a) if a_good else None
            antinodes.add(anti_b) if b_good else None

            if a_good or b_good:
                continue

            break

print("Solution 2:", len(antinodes))
