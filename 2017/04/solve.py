
input = open("04/input.txt").read().splitlines()

res1 = 0
for line in input:
    segemnts = line.split(" ")
    if len(segemnts) == len(set(segemnts)):
        res1 += 1

print(f"1* Result {res1}")

res2 = 0
for line in input:
    segemnts = line.split(" ")
    sorted_segments = ["".join(sorted(list(s))) for s in segemnts]
    if len(sorted_segments) == len(set(sorted_segments)):
        res2 += 1

print(f"2* Result: {res2}")