
def asSet(g):
    (f, t) = g.split("-")
    return  set(range(int(f), int(t)+1))

def explodeAssignments(assignment1, assignment2):
    return (asSet(assignment1), asSet(assignment2))

# Parse input and explode assignment input to sets containing each individual segment
# this is a quite naive/inefficient way to solve the puzzle
groups = [explodeAssignments(*(x.split(","))) for x in open("input", "r").read().split("\n")]

# Part 1 - which group contains the other
oneIncludesTheOther = 0
for (g0, g1) in groups:
    if g0 <= g1 or g1 <= g0:
        oneIncludesTheOther += 1

print(f"Groups where one includes the other: {oneIncludesTheOther}")

# Part 2 - at least one segment is contained in the other
overlapping = 0
for (g0, g1) in groups:
    if len(g0.intersection(g1)) > 0:
        overlapping += 1

print(f"Groups with overlapping segments: {overlapping}")