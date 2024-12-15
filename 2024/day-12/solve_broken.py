
data = [list(x) for x in open("input-test").read().splitlines()]

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
BOUNDX = len(data)
BONUDY = len(data[0])

def snip_points(name, point, plan, known = []):
    known.append(point)
    potential = [(point[0]+d[0], point[1]+d[1]) for d in DIRECTIONS]
    contextual = []
    for p in potential:
        if p[0] < 0 or p[0] > BOUNDX or p[1] < 0 or p[1] > BOUNDY:
            continue

        if p in known:
            continue

        if plan[p[0]][p[1]] == name:
            contextual.extend(snip_points(name, p, plan, known))
    
    return contextual


regions = []
for x, r in enumerate(data):
    for y, p in enumerate(r):
        xx = snip_points(p, (x,y), data)
        print("All", p, " = ", xx)
        input("..")
