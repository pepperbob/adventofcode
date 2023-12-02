# Good Luck

digits = "123456789"
digitsmap = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
input = open("input.txt").read().splitlines()

res = []
for line in input:
    t = []
    for i, d in enumerate(line):
        if d in digits:
            t.append(int(d))
            continue
        
        ## for part 2
        for x in digitsmap:
            if list(x) == list(line)[i:i+len(x)]:
                t.append(digitsmap[x])

    res.append(f"{t[0]}{t[-1]}")

print(sum([int(x) for x in res]))