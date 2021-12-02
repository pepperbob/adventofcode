

data = open("input.txt").read().splitlines()

deers = []
for d in data:
    dd = d.split()

    deer = {
    "name": dd[0],
    "kms": int(dd[3]),
    "fly": int(dd[6]),
    "pause": int(dd[13]),

    "acckm": 0,
    "points": 0
    }
    deers.append(deer)

def move_deer(d, secs):
    runs = secs // (d["fly"] + d["pause"])
    rest = min(secs % (d["fly"] + d["pause"]), d["fly"])
    return (runs * d["fly"] * d["kms"]) + (rest * d["kms"])


dists = []
for d in deers:
    dists.append(move_deer(d, 2503))

print(f"old score: {max(dists)}")

for s in range(1, 2503):
    for d in deers:
        km = move_deer(d, s)
        d["acckm"] = km
    
    leadkm = max([d["acckm"] for d in deers])
    for d in deers:
        if d["acckm"] == leadkm:
            d["points"] += 1

print(f"New score: {max([d['points'] for d in deers])}")