
rows = list(range(128))
cols = list(range(8))

seats = [rows, cols]

lower = lambda ar: ar[0:int(len(ar)/2)]
upper = lambda ar: ar[int(len(ar)/2):len(ar)]

lowerRows = lambda ar: [lower(ar[0]), ar[1]]
upperRows = lambda ar: [upper(ar[0]), ar[1]]
lowerCols = lambda ar: [ar[0], lower(ar[1])]
upperCols = lambda ar: [ar[0], upper(ar[1])]

mapmap = {
    "F": lowerRows,
    "B": upperRows,
    "L": lowerCols,
    "R": upperCols
}

known_seats = []

with open("input.txt") as f:
    for line in f.read().splitlines():
        inter = list(seats)
        for c in line:
            inter = mapmap[c](inter)
        
        known_seats.append([val for sub in inter for val in sub])

ids = []
for s in known_seats:
    ids.append(s[0]*8+s[1])
ids.sort()

print(f"max id {ids[-1]}")

for id in range(ids[0], ids[-1]):
    if(id not in ids):
        print(f"missing {id}")

