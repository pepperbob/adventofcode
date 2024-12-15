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
        elif item_on_new in "[]":
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


    def can_be_moved(self, current, m):
        dir = DIRECTIONS[m]
        cx1,cy1 = current
        if self.warehouse[cx1][cy1] == "#":
            return False

        if self.warehouse[cx1][cy1] == "[":
            cx2,cy2 = cx1,cy1+1
        elif self.warehouse[cx1][cy1] == "]":
            cx2,cy2 = cx1,cy1-1
        elif self.warehouse[cx1][cy1] == ".":
            return True
        else:
            print("Broken Box around", current, ":", self.warehouse[cx1][cy1])
            self.print()
            input("can be moved WTF?")

        nx1, ny1 = cx1 + dir[0], cy1 + dir[1]
        nx2, ny2 = cx2 + dir[0], cy2 + dir[1]

        item_on_n1 = self.warehouse[nx1][ny1]
        item_on_n2 = self.warehouse[nx2][ny2]

        if m in "<>":
            # can be moved if c2 can be moved
            if item_on_n2 == ".":
                return True
            elif item_on_n2 in "[]":
                return self.can_be_moved((nx2,ny2), m)
            elif item_on_n2 == "#":
                return False
        else: 
            # up down
            n1_can_move = item_on_n1 == "." or self.can_be_moved((nx1,ny1),m)
            n2_can_move = item_on_n2 == "." or self.can_be_moved((nx2,ny2),m)
            return n1_can_move and n2_can_move

    def move_item(self, current, m):
        dir = DIRECTIONS[m]
        cx1, cy1 = current

        if self.warehouse[cx1][cy1] == "[":
            print("Coming from left")
            cx2,cy2 = cx1,cy1+1
        elif self.warehouse[cx1][cy1] == "]":
            print("coming from right")
            cx2,cy2 = cx1,cy1-1
        elif self.warehouse[cx1][cy1] == ".":
            return True
        else:
            print("Moving ", current, "to", m)
            self.print()
            input("WTF?")

        nx1, ny1 = cx1 + dir[0], cy1 + dir[1]
        nx2, ny2 = cx2 + dir[0], cy2 + dir[1]

        # can both be moved?
        if m in "<>":
            # left right, if 2 can be moved, one can be moved 
            item_on_new2 = self.warehouse[nx2][ny2] 
            if item_on_new2 in "[]":
                # there is another box, move this first
                if self.move_item((nx2,ny2), m):
                    self.warehouse[nx2][ny2] = self.warehouse[cx2][cy2]
                    self.warehouse[nx1][ny1] = self.warehouse[cx1][cy1]
                    self.warehouse[cx1][cy1] = "."
                    return True
                else:
                    return False
            elif item_on_new2 == "#":
                    # we cannot move both
                    return False
            else:
                print((cx2,cy2), "is expected to be on the other side")
                # clear path for 2 so just move stuff
                self.warehouse[nx2][ny2] = self.warehouse[cx2][cy2]
                self.warehouse[nx1][ny1] = self.warehouse[cx1][cy1]
                # only the closer thing is free now
                self.warehouse[cx1][cy1] = "."
                return True

        else:
            # up down, check both
            item_on_new1 = self.warehouse[nx1][ny1]
            can_move1 = False
            if item_on_new1 == ".":
                can_move1 = True
            elif item_on_new1 in "[]":
                can_move1 = self.can_be_moved((nx1, ny1), m)

            if not can_move1:
                return False

            item_on_new2 = self.warehouse[nx2][ny2]
            can_move2 = False
            if item_on_new2 == ".":
                can_move2 = True
            elif item_on_new2 in "[]":
                can_move2 = self.can_be_moved((nx2, ny2), m)

            if not can_move2:
                return False

            # print("UP DOWN")
            # input("..")
            if item_on_new1 != ".":
                if not self.move_item((nx1,ny1), m):
                    input("EXPECTED 1 to be moved")

            if item_on_new2 != ".":
                if not self.move_item((nx2,ny2), m):
                    input("EXPECTED 2 to be moved")

            print("Moving", (cx1,cy1), "to", (nx1,ny1))
            self.warehouse[nx1][ny1] = self.warehouse[cx1][cy1]
            self.warehouse[cx1][cy1] = "."

            print("Moving", (cx2,cy2), "to", (nx2,ny2))
            self.warehouse[nx2][ny2] = self.warehouse[cx2][cy2]
            self.warehouse[cx2][cy2] = "."

            return True

    def print(self):
        for r in self.warehouse:
            print("".join(r))

    def lantern_gps_goods_locations(self):
        locations = []
        for x, r in enumerate(self.warehouse):
            for y, g in enumerate(r):
                if g == "[":
                    locations.append((x, y))
        return list(map(lambda x: (x[0]*100, x[1]), locations))

translate = {
    "#": "##",
    ".": "..",
    "O": "[]",
    "@": "@."
}
plane = []
for p in raw_plane.splitlines():
    pp = "".join(map(lambda x: translate[x], list(p)))
    plane.append(list(pp))

movements = list("".join(raw_movements.splitlines()))

wh = Warehouse(plane)
wh.print()
input("..")
for i, m in enumerate(movements):
    print("Move (", i, ")", m, ":")
    wh.move_robot(m)
    # wh.print()

sol2 = [sum(x) for x in wh.lantern_gps_goods_locations()]
print("Solution 2", sum(sol2))
