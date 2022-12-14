split = lambda x: x.split(",")
toInt = lambda x: int(x)

def signum(i):
    if i < 0:
        return -1
    return 0 if i == 0 else 1

def positionRange(a, b):
    # inclusive range between "a" and "b", no diagonals
    diffx, diffy = b[0]-a[0], b[1]-a[1]
    positions = [a]
    add = (signum(diffx), signum(diffy))
    for i in range(1, abs(diffx) + abs(diffy)):
        na = (positions[0][0]+add[0]*i, positions[0][1]+add[1]*i)
        positions.append(na)
    positions.append(b)
    return set(positions)

def buildCave(caveWallTuples):
    cave = set()
    for wall in caveWallTuples:
        for x in range(1, len(wall)):
            cave = cave.union(positionRange(wall[x-1], wall[x]))
    
    return cave, max([x[1] for x in cave])

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
puzzleInput = [x.split(" ") for x in open("input", "r").read().replace("-> ", "").split("\n")]
caveDescription = []
for rawPos in puzzleInput:
    caveDescription.append([tuple(map(toInt, corr)) for corr in map(split, rawPos)])

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
