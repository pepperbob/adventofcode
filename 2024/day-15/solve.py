raw_plane, raw_movements = open("input").read().split("\n\n")

DIRECTIONS = {
 "^": (-1,0),
 "<": (0,-1),
 ">": (0,1),
 "v": (1,0)
}

class Warehouse(object):
    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.robot = self.locate_robot()

    def locate_robot(self):
        for x, r in enumerate(self.warehouse):
            for y, p in enumerate(r):
                if p == "@":
                    return (x,y)
        return None

    def move_robot(self, m):
        dir = DIRECTIONS[m]
        cx, cy = self.robot
        nx, ny = cx + dir[0], cy + dir[1]

        item_on_new = self.warehouse[nx][ny]
        if item_on_new == "#":
            ## found a wall just stay where you are
            pass
        elif item_on_new == "O":
            ## item has to move first
            if self.move_item((nx, ny), m):
                self.warehouse[cx][cy] = "."
                self.warehouse[nx][ny] = "@"
                self.robot = (nx, ny)
        else:
            ## path is clear
            self.warehouse[cx][cy] = "."
            self.warehouse[nx][ny] = "@"
            self.robot = (nx, ny)

    def move_item(self, current, m):
        dir = DIRECTIONS[m]
        cx, cy = current
        nx, ny = cx + dir[0], cy + dir[1]
        item_on_new = self.warehouse[nx][ny]
        if item_on_new == "#":
            # item cannot be moved
            return False
        elif item_on_new == "O":
            # other item - move this first
            if self.move_item((nx,ny), m):
                self.warehouse[nx][ny] = "O"
                self.warehouse[cx][cy] = "."
                return True
        else:
            # path clear
            self.warehouse[nx][ny] = "O"
            self.warehouse[cx][cy] = "."
            return True

    def print(self):
        for r in self.warehouse:
            print("".join(r))

    def lantern_gps_goods_locations(self):
        locations = []
        for x, r in enumerate(self.warehouse):
            for y, g in enumerate(r):
                if g == "O":
                    locations.append((x, y))
        return list(map(lambda x: (x[0]*100, x[1]), locations))

plane = []
for p in raw_plane.splitlines():
    plane.append(list(p))
movements = list("".join(raw_movements.splitlines()))

wh = Warehouse(plane)

for m in movements:
    # print("Move ", m)
    wh.move_robot(m)
    # wh.print()
    # input("..")

sol1 = [sum(x) for x in wh.lantern_gps_goods_locations()]
print("Solution 1", sum(sol1))
