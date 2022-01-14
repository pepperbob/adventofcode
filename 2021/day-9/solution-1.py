
def surrounding(matrix, curr):
    up = (max(curr[0]-1, 0), curr[1])
    left = (curr[0], max(curr[1]-1,0))
    right = (curr[0], min(curr[1]+1, len(matrix[0])-1))
    down = (min(curr[0]+1, len(matrix)-1), curr[1])
    
    neighbors = set()
    for pos in [curr, up, left, right, down]:
        neighbors.add(matrix[pos[0]][pos[1]])
    
    return neighbors


theMap = [list(map(int, list(r))) for r in open("input.txt").read().splitlines()]

spots = []
for x, row in enumerate(theMap):
    for y, r in enumerate(row):
        currPos = (x, y)
        surr = surrounding(theMap, currPos)
        if len(surr) > 1 and min(surr) == r:
            spots.append(r)
            print(f"{r} is a lowpoint of {surr} at {currPos}")

print(spots)

print(sum([x+1 for x in spots]))
