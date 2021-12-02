
sweeps = [int(x) for x in open("input-1.txt").read().splitlines()]

increase = 0
for s in zip(sweeps[1:], sweeps):
    if s[0]>s[1]:
        increase = increase + 1

print(f"Increased {increase} times")