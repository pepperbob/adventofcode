
DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]

def find(what, landscape):
    return [[(x,y)] for x in range(len(landscape)) for y in range(len(landscape[0])) if landscape[x][y]==what]

input = [list(x) for x in open("input", "r").read().split("\n")]

# dimensions
dim = [len(input)-1, len(input[0])-1]
posE = find("E", input)[0][0]

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
    observedPaths = startingPoints
    print(f"Start {startingPoints}")

    positionsWeVisited = set()

    areWeDone = False
    iteration = 0
    while True:
        iteration += 1

        numberOfPaths = len(observedPaths)
        nextPaths = []
        
        # iterate through the paths and spawn new paths
        for pathIndex in range(numberOfPaths):
            # currentPos of currentPath
            currentPath = observedPaths[pathIndex]
            lastStep = observedPaths[pathIndex][-1]

            for d in DIRECTIONS:
                nextStep = (lastStep[0]+d[0], lastStep[1]+d[1])
                if nextStep[0]<0 or nextStep[1]<0 or nextStep[0]>dim[0] or nextStep[1]>dim[1]:
                    # out of bounds
                    continue

                if landscape[nextStep[0]][nextStep[1]] > landscape[lastStep[0]][lastStep[1]]+1 or nextStep in positionsWeVisited:
                    # to high or already been there
                    continue
                            
                positionsWeVisited.add(nextStep)

                # spwan new path
                newlySpawned = currentPath+[nextStep]
                nextPaths.append(newlySpawned)
                
                # if we hit posE we're done!
                if nextStep == posE:
                    areWeDone = True
                    break

            if areWeDone:
                break

        # observe new paths form now on
        observedPaths = nextPaths
        
        if areWeDone:
            break

        if iteration % 10 == 0:
            print(f"Observing: {len(observedPaths)} after iteration {iteration}")
    
    return (iteration, observedPaths)

# Part 1
shortest, paths = runFromStartingPoints(find("S", input), makeLandscape(input))
print(f"Part 1 - shortest: {shortest}")

# Part 2
shortest, paths = runFromStartingPoints(find("a", input), makeLandscape(input))
print(f"Part 2 - shortest: {shortest}")
