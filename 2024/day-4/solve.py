
input = open("input").read().splitlines()

directions = [(1,0), (0,1), (1,1), (1,-1), (0,-1), (-1,0), (-1,1), (-1,-1)]
all_positions = [(x, y) for x in range(0, len(input)) for y in range(0, len(input[0]))]

def do_move(pos, move, max_v):
    (x, y) = pos
    (dx, dy) = move
    x += dx
    y += dy
    if x < 0 or y < 0 or x > max_v or y > max_v:
        return None
    else:
        return (x, y)

def direction(a, b):
    (xa, ya) = a
    (xb, yb) = b
    return (xb - xa, yb - ya)

def look_for(char, matrix, pos, dirs):
    potential_pos = list(filter(lambda x: x is not None, [do_move(pos, d, len(matrix)-1) for d in dirs]))
    new_pos = []
    for p in potential_pos:
        if matrix[p[0]][p[1]] == char:
            new_pos.append(p)
    return new_pos

# get starting points: everyhting with "X"
starting_points = [p for p in all_positions if input[p[0]][p[1]] == "X"]
candidates = []

# iterate over starting points, look for M in all directions
for p in starting_points:
    candidates.extend([[p, c] for c in look_for("M", input, p, directions)])

# follow initial direction for AS
for p in candidates:
    dir = direction(p[0], p[-1])
    for letter in "AS":
        p.extend(look_for(letter, input, p[-1], [dir]))

# filter result with 4 hits
res = [p for p in candidates if len(p)==4]

print(f"Solution 1: {len(res)}")

