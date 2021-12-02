

commands = [x.split(" ") for x in open("input.txt").read().splitlines()]

# horizontal, depth, aim
pos = (0,0,0)
for c in commands:
    diff = int(c[1])
    
    if c[0] == "down":
        pos = (pos[0], pos[1], pos[2] + diff)
    elif c[0] == "up":
        pos = (pos[0], pos[1], pos[2] - diff)
    elif c[0] == "forward":
        pos = (pos[0] + diff, pos[1] + (diff*pos[2]), pos[2])

print(f"Result = {pos[0] * pos[1]}")