
parenthesis = {
    "{": "}",
    "<": ">",
    "[": "]",
    "(": ")"
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

input = open("input.txt").read().splitlines()

baum = []
fehler = []
for line in input:
    for k in line:
        if k in parenthesis.keys():
            baum.append(k)
        elif parenthesis[baum.pop()] != k:
            fehler.append(k)
            break

print(sum([points.get(x) for x in fehler]))
# print(sum([points[x] for x in fehler]))