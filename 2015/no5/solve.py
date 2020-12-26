import re

vowels = "aeiou"
forbidden = ("ab", "cd", "pq", "xy")

# count 3 vowels
# letter twice

strings = open("input.txt").read().strip().split("\n")

valid = 0
for string in strings:
    is_valid = True
    for f in forbidden:
        if f in string:
            is_valid = False        
            break
    
    if not is_valid:
        continue
    
    vows = sum([1 for v in string if v in vowels])

    if vows < 3:
        is_valid = False
        continue

    dds = sum([1 for s1, s2 in zip(string, string[1:]) if s1 == s2])

    if dds == 0:
        is_valid = False
        continue

    valid += 1

print(f"Valid {valid}")

valid2 = 0
for string in strings:
    is_valid = False
    dds = sum([1 for a, b, c in zip(string, string[1:], string[2:]) if a == c and a != b])

    if dds > 0:
        is_valid = True
    
    if is_valid:
        pairs = [(a,b) for a,b in zip(string, string[1:])]
        for idx, p in enumerate(pairs):
            if p in pairs[idx+2:]:
                is_valid = True
                break
            else:
                is_valid = False
    
    if is_valid:
        valid2 += 1

# 57
print(f"Valid 2: {valid2}")