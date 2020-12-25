import re

bagregex = re.compile(r"(\d+)\s(.+)");
nootheregex = re.compile(r"no other");

def makebag(bag, content):
    thebag = {
        "name": bag,
        "content": []
    }

    for c in content:
        m = bagregex.match(c)
        if(bool(m)):
            thebag["content"].append({
                "name": m.group(2).strip(),
                "count": int(m.group(1))
            })
    
    return thebag

def digbag(bagname, rules):
    return [bag for bag in rules if bag["name"]==bagname][0]

def bagsize(bagname, rules):
    size = 1
    bag = digbag(bagname, rules)
    print(f"bag = {bag}")
    for c in bag["content"]:
        size += c["count"] * bagsize(c["name"], rules)
    return size

lines = open("input.txt").read().splitlines()

rules = []
for line in lines:
    x = line.replace(".", "").split("contain")
    rules.append(makebag(x[0].replace("bags", "").strip(), x[1].replace("bags", "").replace("bag", "").strip().split(", ")))

size = bagsize("shiny gold", rules)
print(size-1)