from itertools import permutations

data = open("input.txt").read().splitlines()

prep = {}
ppl = set()

for x in data:
    k = x.split(" ")
    who = k[0]
    factor = -1 if k[2] == "lose" else +1
    units = int(k[3])
    other = k[10].replace(".", "")
    ppl.add(who)
    prep[(who,other)] = factor*units
    prep[("me",other)] = 0
    prep[(other,"me")] = 0

def pair_table(t):
    pairs = []
    pairs.append((t[-1],t[0]))
    pairs.append((t[0],t[-1]))
    for a,b in zip(t, t[1:]):
        pairs.append((a,b))
        pairs.append((b,a))
    return pairs

def value_table(t):
    value = 0
    for p in pair_table(t):
        value += prep[p]
    return value

happy = []
for p in list(permutations(ppl)):
    happy.append(value_table(p))

print(max(happy))

ppl.add("me")
happy2 = []
for p in list(permutations(ppl)):
    happy2.append(value_table(p))

print(max(happy2))
