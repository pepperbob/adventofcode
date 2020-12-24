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

passes = []
for line in lines:
    passport = []
    for field in line:
        (k, v) = field.split(":")
        passport.append((k, v))
    passes.append(list(passport))

valid = 0
passes_valid = []
for ppp in passes:
    p = [pp[0] for pp in ppp]

    if(all(elem in p for elem in required)):
        valid = valid + 1
        passes_valid.append(ppp)

print(f"Total Passports: {len(passes)}")
print(f"Valid Passports: {len(passes_valid)}")

def evaluate_field(field, pa):
    f, b = field
    v = True
    if f == "byr":
        v = int(b) >= 1920 and int(b) <= 2002
    elif f == "iyr":
        v = int(b) >= 2010 and int(b) <= 2020
    elif f == "eyr":
        v = int(b) >= 2020 and int(b) <= 2030
    elif f == "hgt":
        if "cm" in b:
            cm = int(b.replace("cm", ""))
            v = cm >= 150 and cm <= 193
        elif "in" in b:
            inch = int(b.replace("in", ""))
            v = inch >= 59 and inch <= 76
        else: 
            v = False
    elif f == "hcl":
        v = bool(re.match(r"^#[0-9a-f]{6}$", b))
    elif f == "ecl":
        v = b in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    elif f == "pid":
        v = bool(re.match(r"^\d{9}$", b))
    
    print(f"{v}: {f} - {b}")
    return v

# part2:
strict_valid = 0
for ppp in passes_valid:
    if(all([evaluate_field(i, ppp) for i in ppp])):
        strict_valid = strict_valid + 1

print(f"Strict Valid: {strict_valid}")

## 37 ist murks
