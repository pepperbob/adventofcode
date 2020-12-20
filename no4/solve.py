import re

required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  

lines = [[]]
pports = []
with open("input.txt", "r") as f:
    for line in f.read().splitlines():
        if(not line):
            lines.insert(0, [])
        else:
            lines[0].extend(line.split(" "))

print(lines)

passes = []
for line in lines:
    passport = []
    for field in line:
        (k, v) = field.split(":")
        passport.append(k)
    passes.append(list(passport))

valid = 0
for p in passes:
    if(all(elem in p for elem in required)):
        print(p)
        valid = valid + 1

print(f"Total Passports: {len(passes)}")
print(f"Valid Passports: {valid}")