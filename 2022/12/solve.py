
DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]

def find(what, landscape):
    return [(x,y) for x in range(len(landscape)) for y in range(len(landscape[0])) if landscape[x][y]==what]

input = [list(x) for x in open("input", "r").read().split("\n")]

# dimensions
dim = [len(input)-1, len(input[0])-1]
posE = find("E", input)[0]

def makeLandscape(input):
    landscape = []
    for x in range(len(input)):
        curr = []
        landscape.append(curr)
        for y in range(len(input[0])):
            height = 0
            if input[x][y] == "E":
                height = ord('z')
            elif input[x][y] == "S":
                height = ord('a')
            else:
                height = ord(input[x][y])
            curr.append(height)    
    return landscape

print(f"Finish {posE}")

def runFromStartingPoints(startingPoints, landscape):
    print(f"Starting from {len(startingPoints)} position/s")
    observedPoints = startingPoints
    pointsWeVisitedAlready = set()

    areWeDone = False
    iteration = 0
    while True:
        iteration += 1

        numberOfPaths = len(observedPoints)
        nextSteps = []
        
        # iterate through the paths and spawn new paths
        for pathIndex in range(numberOfPaths):
            # currentPos of currentPath
            lastStep = observedPoints[pathIndex]

            for d in DIRECTIONS:
                nextStep = (lastStep[0]+d[0], lastStep[1]+d[1])
                if nextStep[0]<0 or nextStep[1]<0 or nextStep[0]>dim[0] or nextStep[1]>dim[1]:
                    # out of bounds
                    continue

                if landscape[nextStep[0]][nextStep[1]] > landscape[lastStep[0]][lastStep[1]]+1 or nextStep in pointsWeVisitedAlready:
                    # to high or already been there
                    continue
                            
                pointsWeVisitedAlready.add(nextStep)

                # continue from here in next iteration
                nextSteps.append(nextStep)
                
                # if we hit posE we're done!
                if nextStep == posE:
                    areWeDone = True
                    break

            if areWeDone:
                break

        # observe new paths form now on
        observedPoints = nextSteps
        
        if areWeDone:
            break
    
    return iteration

# Part 1
print("Part 1")
shortest = runFromStartingPoints(find("S", input), makeLandscape(input))
print(f"Shortest: {shortest} steps")
print("")

# Part 2
print("Part 2")
shortest = runFromStartingPoints(find("a", input), makeLandscape(input))
print(f"Shortest: {shortest} steps")