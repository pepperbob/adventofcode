
input = open("input").read().splitlines()

# diagonals only
directions = [(1,1), (-1,-1), (1, -1), (-1, 1)]
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
    return (abs(xb - xa), abs(yb - ya))

def look_for(char, matrix, pos, dirs):
    potential_pos = list(filter(lambda x: x is not None, [do_move(pos, d, len(matrix)-1) for d in dirs]))
    new_pos = []
    for p in potential_pos:
        if matrix[p[0]][p[1]] == char:
            new_pos.append(p)
    return new_pos

# get starting points: everyhting with "A"
starting_points = [{ "A": p } for p in all_positions if input[p[0]][p[1]] == "A"]

res = []
# iterate over starting points, look for M&S in diagonal direction
for c in starting_points:
    # from A, look for M and S
    p = c["A"]
    c["M"] = look_for("M", input, p, directions)
    c["S"] = look_for("S", input, p, directions)

    # check rules and ignore if not met
    if len(c["M"]) != 2 or len(c["S"]) != 2:
        # ignore, no x-mas here 
        continue;

    if direction(c["M"][1], c["M"][0]) not in [(2,0), (0,2)]:
        # ignore, no x-mas here
        continue;

    if direction(c["S"][1], c["S"][0]) not in [(2,0), (0,2)]:
        # ignore, no x-mas here
        continue;

    # well done, this is x-mas
    res.append(c)

print("Solution 2: ", len(res))
