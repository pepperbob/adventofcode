
input = [int(x) for x in open("05/input").read().splitlines()]

def steps_throug_maze_till_end(maze, addoffset = lambda x: 1):
    iteration = 0
    pos = 0
    exit_after = len(maze)
    while True:
        iteration += 1

        nxt = maze[pos]
        maze[pos] += addoffset(maze[pos])
        pos += nxt
        if pos < 0 or pos >= exit_after:
            break
    return iteration

res1 = steps_throug_maze_till_end(input.copy())
print(f"1* Result: {res1}")

res2 = steps_throug_maze_till_end(input.copy(), lambda x: -1 if x > 2 else 1)
print(f"1* Result: {res2}")