import re

grid = [[0 for i in range(1000)] for j in range(1000)]

def resolve(rang):
    from_pos = rang[0]
    to_pos = rang[1]

    x = from_pos[0]

    while x <= to_pos[0]:

        y = from_pos[1]
        while y <= to_pos[1]:
            yield (x, y)
            y += 1
        x +=1

def turn_on(rang, matrix):
    for pos in resolve(rang):
        matrix[pos[0]][pos[1]] += 1


def turn_off(rang, matrix):
    for pos in resolve(rang):
        curr = matrix[pos[0]][pos[1]]
        matrix[pos[0]][pos[1]] = curr - 1 if curr > 0 else 0

def toggle(rang, matrix):
    for pos in resolve(rang):
        matrix[pos[0]][pos[1]] += 2

ops = open("input.txt").read().strip().split("\n")

for op in ops:
    ranges = re.findall(r"(\d{1,},\d{1,})", op)

    assert len(ranges) == 2, f"Range to small... {ranges}"

    from_pos = tuple(map(lambda x: int(x), ranges[0].split(",")))
    to_pos = tuple(map(lambda x: int(x), ranges[1].split(",")))
    
    if op.startswith("turn on"):
        turn_on((from_pos, to_pos), grid)
    elif op.startswith("turn off"):
        turn_off((from_pos, to_pos), grid)
    elif op.startswith("toggle"):
        toggle((from_pos, to_pos), grid)

# too low 14230241
print(sum([j for i in grid for j in i if j >= 0]))