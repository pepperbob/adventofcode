
def within_bounds(bound, pos):
    lx, ly = bound[0]
    ux, uy = bound[1]
    x, y = pos
    return x > lx and x < ux and y > ly and y < uy

def print_map(arr2d):
    for x in arr2d:
        print(x)

def locate(char, arr2d):
    for x, xc in enumerate(arr2d):
        for y, yc in enumerate(xc):
            if yc == "^":
                return (x, y)
    return None

def move(from_pos, dirs, arr2d):
    xdirs = dirs[:]
    dx, dy = xdirs[0]
    x, y = from_pos
    mx, my = (x+dx, y+dy)
    if arr2d[mx][my] != "#":
        arr2d[x][y] = "X"
        arr2d[mx][my] = "^"

        return ((mx,my), dirs, arr2d)
    else:
        xdirs.append(xdirs.pop(0))
        return move(from_pos, xdirs, arr2d)

# up, right, down, left // 90°
origin_directions = [(-1,0), (0,1), (1,0), (0,-1)]
origin_map = [list(i) for i in open("input").read().splitlines()]

directions = [d for d in origin_directions]
the_map = [row[:] for row in origin_map]
bounds = ((0,0), (len(the_map)-1, len(the_map[0])-1))
guard = locate("^", the_map) 
visited_positions = []
while within_bounds(bounds, guard):
    guard, directions, _  = move(guard, directions, the_map)
    # print_map(the_map)
    # print("Guard is at" , guard)
    visited_positions.append(guard) 
    # input("..")

print("Solution 1:", len(set(visited_positions)))


def put_obstacle(pos, the_map):
    new_map = [x[:] for x in the_map]
    new_map[pos[0]][pos[1]] = "#"
    return new_map

guard_start = locate("^", origin_map)
loop_count = 0
for v in set(visited_positions):
    # obstacle must be on the guards path so brute force every single position
    obstacled_map = put_obstacle(v, origin_map)
    guard = guard_start
    directions = origin_directions
    loop_detector = {}

    while within_bounds(bounds, guard):
        guard, directions, _ = move(guard, directions, obstacled_map)
        loop_detector[guard] = loop_detector.get(guard, 0) + 1

        # approximation for infinity
        if loop_detector[guard] > 5:
            # print("Found loop", loop_detector)
            print("Loop Found: ", guard)
            # print_map(obstacled_map)
            loop_count += 1
            break;

        # print_map(obstacled_map)
        # input("..")

print("Solution 2:", loop_count)

