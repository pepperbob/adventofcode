import itertools as it


raw = [list(x) for x in open("11/input").read().splitlines()]

def add_gravitational_lensing(space):
    """ add an "empty" row where there is an empty row
    """
    real_space = []
    for r in space:
        # empty row check
        if len(set(r)) == 1 and r[0] == ".":
            real_space.append(r.copy())
        real_space.append(r)
    return real_space

def makeLists(xxx):
    for i in xxx:
        yield list(i)

real_space = add_gravitational_lensing(raw)
real_space = add_gravitational_lensing(list(makeLists(zip(*real_space[::-1]))))

galaxies  = []
for x, xx in enumerate(real_space):
    for y, yy in enumerate(xx):
        if yy == "#":
            galaxies.append((x,y))

res = 0
for g1, g2 in it.combinations(galaxies, 2):
    res += abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])

print(f"1* Result: {res}")
