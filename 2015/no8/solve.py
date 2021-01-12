import re

lines = open("input.txt").read().strip().split("\n")

total = len([c for line in lines for c in line])
print(total)

effective = 0
for line in lines:
    effective += eval(f"len({line})")

print(f"{effective} ")
print(total - effective)

total2 = 0
for line in lines:
    cc = "\""
    for c in line:
        if c in "\"\\":
            cc += f"\{c}"
        else:
            cc += c
    cc += "\""
    total2 += len(cc)

print(total2 - total)

