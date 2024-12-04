import re

input = open("input").read()

res = [int(x)*int(y) for (x, y) in re.findall("mul\((\d+),(\d+)\)", input)]

print(f"Solution 1: {sum(res)}")
