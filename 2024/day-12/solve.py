
data = [list(x) for x in open("input").read().splitlines()]

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
BOUNDX = len(data)
BOUNDY = len(data[0])

class Region(object):

    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.orig = None
        self.orig = self.matrix()

    def area(self):
        return len(self.points)

    def perimeter(self):
        return len([s for s in self.surrounding(self.points) if s not in self.points])

    def surrounding(self, matrix):
        return [(p[0]+d[0], p[1]+d[1]) for p in matrix for d in DIRECTIONS]

    def matrix(self):
        # populate a 2d array with the region framed in space (.) and centered
        if self.orig:
            p, X, Y = self.orig
            return ([o[:] for o in p], X, Y)

        minx = min([x[0] for x in self.points])-1
        miny = min([x[1] for x in self.points])-1

        maxx = max([x[0] for x in self.points])+2-minx
        maxy = max([x[1] for x in self.points])+2-miny

        canvas = [["." for y in range(maxy)] for x in range(maxx)]

        for (x, y) in self.points:
            canvas[x-minx][y-miny] = self.name

        return (canvas, maxx, maxy)

    def print(self, pos = None, character = "*"):
        M, _, _ = self.matrix()
        if pos is not None:
            M[pos[0]][pos[1]] = character

        for r in M:
            print(" ".join(r)) 

    def sides(self):
        window = [(0,0), (0,1), (1,0), (1,1)]
        plane, X, Y = self.matrix()
        corners = 0
        ## move window of 2x2
        for x in range(X-1):
            for y in range(Y-1):
                # select items in window
                window_select = {(w[0]+x,w[1]+y): plane[w[0]+x][w[1]+y] for w in window}
                window_values = [v for v in window_select.values()]
                elements = {i: window_values.count(i) for i in window_values}
                
                # if there are not dots, then there is no corner
                if "." not in elements:
                    continue

                if elements["."] == 3 or elements["."] == 1:
                    # 1 or 3 dots: definitely a corner
                    corners += 1
                elif elements["."] == 2:
                    # 2 corners if diagonal
                    s1,s2 = [k for k in window_select.keys() if window_select[k] == "."]
                    if s1[0] != s2[0] and s1[1] != s2[1]:
                        corners += 2

        return corners

    def __repr__(self):
        return f"Region {self.name}"

def snip_points(name, point, plan, known = []):
    known.append(point)
    potential = [(point[0]+d[0], point[1]+d[1]) for d in DIRECTIONS]
    contextual = [point]
    for p in potential:
        if p[0] < 0 or p[0] >= BOUNDX or p[1] < 0 or p[1] >= BOUNDY:
            continue

        if p in known:
            continue

        if plan[p[0]][p[1]] == name:
            contextual.extend(snip_points(name, p, plan, known))
    return contextual

regions = []
known = []
for x, r in enumerate(data):
    for y, p in enumerate(r):
        point = (x, y)
        if point in known:
            continue

        xx = snip_points(p, point, data)
        known.extend(xx)
        regions.append(Region(p, xx))

# solution1 = sum([r.area()*r.perimeter() for r in regions])
# print("Solution 1", solution1)
print("There are", len(regions), "regions")
prices = []
for i, r in enumerate(regions):
    print("Region", i)
    prices.append(r.area() * r.sides())

solution2 = sum(prices)
print("Solution 2", solution2)
