import re

# read input
input = [re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", x) for x in open("input.txt").readlines()]
# map to ints 0-4
raw = [list(map(int, y)) for x in input for y in x if y[0] == y[2] or y[1] == y[3]]
# map to coordinates
coordinates = [[tuple(c[:2]), tuple(c[2:])] for c in raw]

# build plane of stuff, size just enough...
plane = [[0 for col in range(1000)] for row in range(1000)]

def point_range(pointX, pointY):
    fromX0 = min(pointX[0], pointY[0])
    toY0 = max(pointX[0], pointY[0])

    fromX1 = min(pointX[1], pointY[1])
    toY1 = max(pointX[1], pointY[1])
    
    for x in range(fromX0, toY0+1):
        for y in range(fromX1, toY1+1):
            yield (x, y)

for c in coordinates:
    pointX = c[0]
    pointY = c[1]

    for p in point_range(c[0], c[1]):
        plane[p[0]][p[1]] = plane[p[0]][p[1]] + 1

res = [k for x in plane for k in x if k > 1]
print(f"Intersections: {len(res)}")