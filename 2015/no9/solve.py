import itertools

distances = open("input.txt").read().strip().split("\n")

dists = {}
locs = set()
for dist in distances:
    dd, km = dist.split("=")
    f,t = dd.split("to")

    dists[(f.strip(),t.strip())]=int(km) 
    dists[(t.strip(),f.strip())]=int(km) 
    locs.add(t.strip())
    locs.add(f.strip())

# generate all combinations of cities
routes = []
for p in list(itertools.permutations(locs)):
    # add distances pairwise
    dist = 0
    for a, b in zip(p, p[1:]):
        dist += dists[(a,b)]
    routes.append(dist)

print(f"Shortest: {min(routes)}")
print(f"Shortest: {max(routes)}")