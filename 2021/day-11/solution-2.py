
input = [list(map(int, list(x))) for x in open("input.txt").read().splitlines()]

directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]

def neighbor_pos(arr, pos = (0,0)):
    lenx = len(arr)
    leny = len(arr[0])

    neighbors = set()
    for d in directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])
        if new_pos[0] >= 0 and new_pos[0] < lenx and new_pos[1] >= 0 and new_pos[1] < leny:
            neighbors.add(new_pos)

    return neighbors

def increase_by_one(input, pos):
    energy = input[pos[0]][pos[1]] + 1
    input[pos[0]][pos[1]] = energy
    if energy == 10:
        for p in neighbor_pos(input, pos):
            increase_by_one(input, p)


flashed = 0
for n in range(1000):
    
    # increase by one
    for x, i in enumerate(input):
        for y, ii in enumerate(i):
            increase_by_one(input, (x, y))

    for x, i in enumerate(input):
        for y, ii in enumerate(i):
            if ii > 9:
                flashed += 1
                input[x][y] = 0

    if sum([y for x in input for y in x]) == 0:
        print(n+1)
        break
