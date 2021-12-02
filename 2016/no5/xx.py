from collections import Counter

input = open("input.txt").read().splitlines()

iinput = [[] for x in range(0,8)]

for x in input:
    for k, xx in enumerate(x):
        iinput[k].append(xx)


print("".join([min(c,key=c.count) for c in iinput]))
