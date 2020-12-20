import re

def reversefindbag(bag, rules):
    bags = [r["bag"] for r in rules if bool(re.search(bag, r["content"]))]
    for b in list(bags):
        print(f"Reverse look for: {b}")
        bags.extend(reversefindbag(b, rules))
    return set(bags)

lines = open("input.txt").read().splitlines()

rules = []
for line in lines:
    x = line.split("contain")
    rules.append({
        "bag": x[0].replace("bags", "").strip(),
        "content": x[1].strip()
    })


shiny_gold = reversefindbag("shiny gold", rules)
print(len(shiny_gold))
