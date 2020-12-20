import re

lines = []
with open("input.txt", "r") as f:
    for l in f.readlines():
        rule = re.split("[\s-]", l.replace("\n", "").replace(":", ""))
        splits = list(rule[3])
        lo = int(rule[0])
        up = int(rule[1])
        pos = ""
        pos += splits[lo-1]
        pos += splits[up-1]
        
        print(pos)

        if(pos.count(rule[2]) == 1):
            lines.append(l)
        """ if(occ >= lo and occ <= up):
            lines.append({
                "should": f"{lo}-{up}",
                "is": occ,
                "letter": rule[2],
                "pass": rule[3]
            }) """

print(f"{len(lines)} are valid")
