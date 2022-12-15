import re

def distance(a, b):
    ax, ay = a
    bx, by = b
    return abs(ax-bx) + abs(ay-by)

def isInRadius(a, radius, b):
    return distance(a, b) <= radius

def rangeIncluding(a: int):
    return range(-a, a+1)

pattern = re.compile(r"x=(-?\d+),\sy=(-?\d+):.+x=(-?\d+),\sy=(-?\d+)")
sensorsbeacons = [list(map(int, x[0])) for x in [pattern.findall(x) for x in open("input", "r").read().strip().split("\n")]]


def part1(sensorsbeacons):
    allbeacons = set([(bx, by) for _,_,bx,by in sensorsbeacons])
    allsensors = set([(sx, sy) for sx,sy,_,_ in sensorsbeacons])

    row = 2000000

    nobeacons = set()
    for sb in sensorsbeacons:
        sx, sy, bx, by = sb
        sensor = (sx, sy)

        sensorRadius = distance(sensor, (bx, by))
        distanceToRow = abs(sy - row)

        if distanceToRow <= sensorRadius:
            rowsFromMaxRadius = abs(distanceToRow - sensorRadius)
            sensorShadow = [(sx+a, row) for a in range(-rowsFromMaxRadius, rowsFromMaxRadius+1)]
            nobeacons |= set([x for x in sensorShadow if x not in allbeacons and x not in allsensors])

    print(f"Beancons cannot be: {len(nobeacons)}")

x = 4*10**6

print(x)