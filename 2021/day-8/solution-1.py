import re

numbers = {
    2: 1,
    3: 7,
    4: 4,
    7: 8
}

lines = [re.findall(r"\|\s*(.+)$", x) for x in open("input.txt").readlines()]
segments = [x.split(" ") for l in lines for x in l]
segments_of_interest = [y for x in segments for y in x if len(y) in numbers.keys()]

print(segments_of_interest)
print(len(segments_of_interest))