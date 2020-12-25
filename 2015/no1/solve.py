

ops = list(open("input.txt").read().strip())

acc = 0
basement_at = None
for i, op in enumerate(ops):
    if op == "(":
        acc += 1
    else:
        acc += -1
    
    if basement_at == None and acc == -1:
        basement_at = i + 1

print(f"Result 1: {acc}")
print(f"Result 2: {basement_at}")