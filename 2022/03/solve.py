
items = list("_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def priority(c):
    return items.index(c)

def compartments(rucksack):
    s = int(len(rucksack)/2)
    return (rucksack[0:s], rucksack[s:])

def duplicateItemOf(rucksack):
    (c1, c2) = compartments(rucksack)
    return next(iter([i for i in c1 if i in c2]), None)

rucksacks = open("input", "r").read().split("\n")

# Part 1: sum priorities of duplicate items in rucksack
priorities = [priority(duplicateItemOf(rucksack)) for rucksack  in rucksacks]
print(f"Sum of priorities: {sum(priorities)}")

# Part 2: sum priorities of the badge of group of 3
def badgeOf(groupOfRucksacks):
    (r1, r2, r3) = groupOfRucksacks
    return next(iter([i for i in r1 if i in r2 and i in r3]), None)

currentGroup = []
groupweights = []
for r in rucksacks:
    currentGroup.append(r)
    if len(currentGroup) == 3:
        groupweights.append(priority(badgeOf(currentGroup)))
        currentGroup = []

print(f"Sum of group badges: {sum(groupweights)}")