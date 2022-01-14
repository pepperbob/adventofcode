
from types import coroutine


with open("input.txt") as f:
    input = f.read().splitlines()

coordinates = [(int(k[0]), int(k[1])) for k in map(lambda x : x.split(","),  [i for i in input if "," in i])]
maxx = max([k[0] for k in coordinates])
maxy = max([k[1] for k in coordinates])

start_arr = [["." for y in range(maxy+1)] for x in range(maxx+1)]

cmds = [i for i in input if "," not in i and len(i) > 0]

for i in coordinates:
    start_arr[i[0]][i[1]] = "#"

for x in start_arr:
    print(x)