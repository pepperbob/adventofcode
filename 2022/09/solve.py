
input = [(x[0], int(x[1])) for x in [x.split(" ") for x in open("input", "r").read().split("\n")]]

movements = {
    "R": lambda old: (old[0], old[1]+1),
    "L": lambda old: (old[0], old[1]-1),
    "U": lambda old: (old[0]+1, old[1]),
    "D": lambda old: (old[0]-1, old[1])
}

def signum(i):
    if i == 0:
        return 0
    return -1 if i < 0 else 1

def signumPos(pos):
    return (signum(pos[0]), signum(pos[1]))

def diffPosition(left, right):
    return (left[0]-right[0], left[1]-right[1])

def addPos(pos, diff):
    return (pos[0]+diff[0], pos[1]+diff[1])

def notTouching(left, right):
    diff = diffPosition(left, right)
    return abs(diff[0])>1 or abs(diff[1])>1

def doMove(rope, allMoves):
    tailPositions = []

    for move, times in allMoves:

        for t in range(times):
            head = rope[0]
            rope[0] = movements[move](head)
            
            for idx in range(1, len(rope)):
                prev = rope[idx-1]
                knot = rope[idx]

                if notTouching(prev, knot):
                    rope[idx] = addPos(knot, signumPos(diffPosition(prev, knot)))

                if idx == len(rope)-1:
                    tailPositions.append(rope[idx])

    return set(tailPositions)

# part 1
part1 = doMove(rope=[(0,0)]*2, allMoves=input)
print(len(part1))

# part 2
part2 = doMove(rope=[(0,0)]*10, allMoves=input)
print(len(part2))
