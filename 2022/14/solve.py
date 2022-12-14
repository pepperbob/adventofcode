split = lambda x: x.split(",")

def signum(i):
    return (0<i)-(i<0)

def positionRange(a, b):
    # inclusive range between "a" and "b", no diagonals
    ax, ay = a
    diffx, diffy = b[0]-ax, b[1]-ay
    addx, addy = (signum(diffx), signum(diffy))
    positions = set([a, b])
    for i in range(1, abs(diffx) + abs(diffy)):
        positions.add((ax+addx*i, ay+addy*i))
    return positions

def buildCave(caveWallTuples):
    cave = set()
    for wall in caveWallTuples:
        for x in range(1, len(wall)):
            cave |= positionRange(wall[x-1], wall[x])

    return cave, max(y for _, y in cave)

def letSandSink(cave, deepest, behindDeepest):    
    newSand = ENTRY
    while True:
        # move down
        currentSand = newSand
        newSand = (currentSand[0], currentSand[1]+1)

        # deepest + 2 is hard limit
        if newSand[1] == deepest + 2:
            return behindDeepest(currentSand)

        if newSand in cave:
            # move left
            newSand = (newSand[0]-1, newSand[1])
            if newSand in cave:
                # move right
                newSand = (newSand[0]+2, newSand[1])
                if newSand in cave:
                    break
    
    return currentSand

# Setup - the most stupid code
caveDescription = []
for rawPos in [x.split(" ") for x in open("input", "r").read().replace("-> ", "").split("\n")]:
    caveDescription.append([tuple(map(int, corr)) for corr in map(split, rawPos)])

ENTRY = (500, 0)
ABYSS = lambda c: None
FLOOR = lambda c: c

# Part 1
theCave, deepest = buildCave(caveDescription)
sandUnits = 0
while True:
    newSand = letSandSink(theCave, deepest, behindDeepest=ABYSS)
    
    if newSand is None:
        break

    sandUnits += 1
    theCave.add(newSand)
print(f"Part 1, Sand Units = {sandUnits}")

# Part 2
theCave, deepest = buildCave(caveDescription)
sandUnitsFit = 0
while True:
    newSand = letSandSink(theCave, deepest, behindDeepest=FLOOR)
    sandUnitsFit += 1

    if newSand == ENTRY:
        break
    
    theCave.add(newSand)
print(f"Part 2, Sand Units Fit = {sandUnitsFit}")
