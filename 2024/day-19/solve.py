from functools import cache

towels, patterns = open("input").read().split("\n\n")
towels = towels.split(", ")
patterns = patterns.splitlines()

@cache
def check_pattern(pat):
    if pat == "":
        return 1

    tot = 0
    for t in towels:
        if pat.startswith(t):
            tot += check_pattern(pat.removeprefix(t))
    return tot

tot = 0
for p in patterns:
    tot += check_pattern(p)

print(tot)
