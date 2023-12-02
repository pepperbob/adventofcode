import math

rawinput = open("02/input.txt").read().splitlines()

# sets of (game string, list of draws)
input=[]
for line in rawinput:
    game, rest = line.split(":")
    draws = [d.split(",") for d in rest.split(";")]
    input.append((game, draws))

cubecount = {"red": 12, "green": 13, "blue": 14}
def game_num_if_possible(gamestr, drawslist):
    for draw in drawslist:
        for d in draw:
            count, color = d.strip().split(" ")
            if cubecount[color.strip()] < int(count):
                return 0
    return int(gamestr.split(" ")[1])

def power_least_possible(drawslist):
    least_cubes = dict()
    for draw in drawslist:
        for d in draw:
            count, color = d.strip().split(" ")
            if color in least_cubes:
                least_cubes[color] = max(least_cubes[color], int(count))
            else:
                least_cubes[color] = int(count)
    return math.prod(least_cubes.values())

# Part 1
res1 = 0
res2 = 0
for i in input:
    game, draws = i
    res1 += game_num_if_possible(game, draws)
    res2 += power_least_possible(draws)

print(f"1* Result: {res1}") 
print(f"2* Result: {res2}") 
