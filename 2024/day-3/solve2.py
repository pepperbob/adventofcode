import re

input = open("input").read()

tuples = re.findall("((mul)\((\d+),(\d+)\)|(do)\(\)|((don\'t)\(\)))", input)

capture = True
res = []
for t in tuples:
    print(t)
    if t[4] == "do":
        capture = True
    elif t[6] == "don't":
        capture = False
    elif capture == True:
        res.append(int(t[2])*int(t[3]))

print(f"Solution 2: {sum(res)}")

