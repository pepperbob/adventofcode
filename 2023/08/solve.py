import numbers, math

data = open("08/input").read().splitlines()

instruction = data[0]

network = dict()

for a,b in [x.split("=") for x in data[2:]]:
    refs = b[2:-1].split(",")
    network[a.strip()] = [y.strip() for y in refs]

res = 0
instlen = len(instruction)
last = "AAA"
while last != "ZZZ":
    if last not in network.keys():
        break
    last_idx = 0 if instruction[res%instlen] == "L" else 1
    last = network[last][last_idx]
    res+=1

print(f"1* Result: {res}")

# part 2 won't scale by just walking through it
# solution: walk individual and stop when Z is found
# guess: it repeats
j = 0
starting_pos = [[(x, instruction[0])] for x in network.keys() if x[-1] == "A"]
while True:
    repeat = False
    j += 1
    for tracked in starting_pos:
        if isinstance(tracked[-1], numbers.Number):
            continue

        last = tracked[-1] # last tracked
        last_idx = 0 if last[1] == "L" else 1
        
        # calc next for each tracked
        next = network[last[0]][last_idx]
        op_next = instruction[j%instlen]
        next_tuple = (next, op_next)

        if next[-1] == "Z":
            tracked.append(j)
        else:
            tracked.append(next_tuple)

    # if all end with numnber quit
    if all([isinstance(x[-1], numbers.Number) for x in starting_pos]):
        break

# calculate least common multiple to calculate when all and in Z
res2 = math.lcm(*[x[-1] for x in starting_pos])
print(f"2* Result: {res2}")
