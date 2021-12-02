
sweeps = [int(x) for x in open("input-1.txt").read().splitlines()]


measurements = [sum(x) for x in zip(sweeps, sweeps[1:], sweeps[2:])]

increase = 0
for s in zip(measurements[1:], measurements):
    if s[0]>s[1]:
        increase = increase + 1

print(f"Increased {increase} times")