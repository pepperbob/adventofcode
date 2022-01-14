
def surroundingPos(matrix, curr):
    up = (max(curr[0]-1, 0), curr[1])
    left = (curr[0], max(curr[1]-1,0))
    right = (curr[0], min(curr[1]+1, len(matrix[0])-1))
    down = (min(curr[0]+1, len(matrix)-1), curr[1])

    return set([up, right, down, left])

def surrounding(matrix, curr):
    neighbors = set()
    for pos in surroundingPos(matrix, curr):
        neighbors.add(matrix[pos[0]][pos[1]])

    neighbors.add(matrix[curr[0]][curr[1]])
    return neighbors


theMap = [list(map(int, list(r))) for r in open("input.txt").read().splitlines()]

lowPoints = []
for x, row in enumerate(theMap):
    for y, r in enumerate(row):
        currPos = (x, y)
        surr = surrounding(theMap, currPos)
        if len(surr) > 1 and min(surr) == r:
            lowPoints.append(currPos)

print(lowPoints)

def findBasin(mm, lp, acc = list()):
    height = mm[lp[0][lp[1]]]
    nbs = surroundingPos(mm, lp)
    
    for n in nbs:
        if mm[n[0]][n[1]] == height + 1:
            acc.append(n)
            findBasin(mm, n, acc)

basins = []
for lp in lowPoints:
    cb = [lp]
    basins.append(cb)
    findBasin(theMap, lp, cb)

print(basins)