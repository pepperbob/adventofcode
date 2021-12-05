import re

# read input
input = [re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", x) for x in open("input.txt").readlines()]
# map to ints 0-4
raw = [list(map(int, y)) for x in input for y in x]
# map to coordinates
coordinates = [[tuple(c[:2]), tuple(c[2:])] for c in raw]

# build plane of stuff, size just enough...
plane = [[0 for col in range(1000)] for row in range(1000)]

def point_range(point1, point2):
    # assumes it moves only in vertical, horizontal or diagonal with slope 1 directions
    
    # how far we need to go
    diffX = point2[0] - point1[0]
    diffY = point2[1] - point1[1]

    # how many steps we need to take: diffX is 0, diffY is 0 or both are the same
    iterations = max(abs(diffX), abs(diffY))

    # direction for each axis: -1, 0 or +1
    directionX = 0 if diffX == 0 else diffX / abs(diffX)
    directionY = 0 if diffY == 0 else diffY / abs(diffY)

    for i in range(iterations+1):
        yield (int(point1[0] + directionX*i), int(point1[1] + directionY*i))

for c in coordinates:
    for p in point_range(c[0], c[1]):
        plane[p[0]][p[1]] = plane[p[0]][p[1]] + 1

res = [k for x in plane for k in x if k > 1]
print(f"Intersections: {len(res)}")