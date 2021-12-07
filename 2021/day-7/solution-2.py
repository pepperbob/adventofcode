

positions = list(map(int, open("input.txt").readline().split(",")))

minpos = min(positions)
maxpos = max(positions)

diffs = []
for i in range(minpos, maxpos+1):
    # abs(x-i) = n, n-1+n-2+n-3 ... 1
    diffs.append(sum([int(abs(x-i)*(abs(x-i)+1)/2) for x in positions]))

print(f"Cheapest is {min(diffs)}")