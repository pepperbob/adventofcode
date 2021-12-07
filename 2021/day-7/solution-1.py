

positions = list(map(int, open("input.txt").readline().split(",")))

minpos = min(positions)
maxpos = max(positions)

diffs = []
for i in range(minpos, maxpos+1):
    diffs.append(sum([abs(x-i) for x in positions]))

print(f"Cheapest is {min(diffs)}")