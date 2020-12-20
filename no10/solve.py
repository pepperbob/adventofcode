
adapters = [int(i) for i in open("input.txt").read().splitlines()]
adapters.sort()

diffs = []

print(adapters)
for idx, jolt in enumerate(adapters):
    if(idx==0):
        diffs.append(jolt)
    else:
        diffs.append(jolt-adapters[idx-1])

diffs.append(3)

print(diffs.count(3) * diffs.count(1))
