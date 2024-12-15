
data = [list(x) for x in open("input").read().splitlines()]

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DIR_MAP = {
    "R": (0, 1),
    "D": (1,0),
    "L": (0,-1),
    "U": (-1,0)
}
SOLID = {
    "R": "D",
    "D": "L",
    "L": "U",
    "U": "R"
}
RLOOK = {
    (0,1): "R",
    (1,0): "D",
    (0,-1): "L",
    (-1,0): "U"
}
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
        ##  self.print()
        for x in range(X-1):
            for y in range(Y-1):
                window_select = {(w[0]+x,w[1]+y): plane[w[0]+x][w[1]+y] for w in window}
                window_values = [v for v in window_select.values()]
                elements = {i: window_values.count(i) for i in window_values}

                if "." not in elements:
                    continue

                if elements["."] == 3 or elements["."] == 1:
                    corners += 1
                elif elements["."] == 2:
                    # check if diagonal
                    s1,s2 = [k for k in window_select.keys() if window_select[k] == "."]
                    if s1[0] != s2[0] and s1[1] != s2[1]:
                        # print(s1, "and", s2, "are diagonal")
                        # input()
                        corners += 2
        return corners

    def walk_around(self):
        # walk the outside
        dirs = list("RDLU") 
        plane, X, Y = self.matrix()
        starting_point = (0, plane[1].index(self.name))
        current_pos = starting_point
        turning = False
        turn_count = 0
        visited = []
        # self.print(current_pos)
        # print("Will start at", starting_point)
        # input("..") 
        while True:
            if starting_point in visited:
                break

            current_dir = DIR_MAP[dirs[0]]
            solid_dir = DIR_MAP[SOLID[dirs[0]]]
            cx, cy = current_pos

            nx = cx + current_dir[0]
            ny = cy + current_dir[1]

            sx = cx + solid_dir[0]
            sy = cy + solid_dir[1]

            # checks
            oo_bounds = nx < 0 or nx >= X or ny < 0 or ny >= Y 
            path_blocked = not oo_bounds and plane[nx][ny] != "."
            lost_wall = not turning and plane[sx][sy] == "."
            # try harder
            been_there = (nx,ny) in visited and turn_count < 4
            try_harder = False
            if turn_count >= 4 and not path_blocked and (nx,ny) in visited:

                # print("Next might be", (nx,ny))
                all = [(cx+d[0], cy+d[1]) for d in DIRECTIONS]  
                # favor position you have been earlier
                alt = [d for d in all if d != (nx,ny) and plane[d[0]][d[1]] == "." ]
                if alt and visited.index(alt[0]) < visited.index((nx,ny)):
                    # fix to favor this
                    nx, ny = alt[0]
                else:
                    pass
                    #print("No alternative")

            if oo_bounds or path_blocked or lost_wall or been_there:
                # turn
                dirs.append(dirs.pop(0))
                turning = True
                turn_count += 1
                if turn_count >= 8:
                    self.print(current_pos)
                    input("stuck?")
                continue
            # check if we stick to the wall
            else:
                turning = False
                turn_count = 0
                current_pos = (nx, ny)
                visited.append(current_pos)

        # input("..")
        return set(visited)

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
