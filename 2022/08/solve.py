

# Directions to move
LEFT, RIGHT, TOP, DOWN = (0, -1), (0, 1), (-1, 0), (1, 0)

# The Forrest
forrest = [list(map(int, list(x))) for x in open("input", "r").read().split("\n")]
dimX, dimY = len(forrest), len(forrest[0])

def isOnEdge(pos):
    return any(map(lambda x: x == 0 or x in (dimX-1, dimY-1), pos))

# recursively go in a direction until edge or tree same size
def go(pos, dir, forrest, initialHeight=None):
    if isOnEdge(pos):
        return pos

    (x, y) = pos
    initialHeight = forrest[x][y] if initialHeight is None else initialHeight
    newX, newY = x+dir[0], y+dir[1]
    
    return pos if forrest[newX][newY]>=initialHeight else go((newX, newY), dir, forrest, initialHeight)

def maxInAnyDir(pos, forrest):
    return map(lambda dir: go(pos, dir, forrest), [LEFT, RIGHT, TOP, DOWN])

allPositions = [(a, b) for a in range(0, dimX) for b in range(0, dimY)]

# part 1
countVisible = 0
for p in allPositions:
    # for position p move as far in all directions and check if max pos is on edge
    isVisible = any(map(isOnEdge, maxInAnyDir(p, forrest)))
    if isVisible:
        countVisible += 1

print(f"Part 1: visible = {countVisible}")

# part 2
import math 
def scenicScore(pos):
    def calcScore(dist):
        add = 0 if isOnEdge(dist) else 1
        totalDist = add+abs(pos[0]-dist[0])+abs(pos[1]-dist[1])
        return totalDist
    return calcScore

maxScore = 0
for p in allPositions:
    currScore = math.prod(map(scenicScore(p), maxInAnyDir(p, forrest)))
    maxScore = max(maxScore, currScore)

print(f"Part 2: max. score = {maxScore}")