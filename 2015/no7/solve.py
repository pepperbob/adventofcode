from collections import defaultdict

result = {}

def what_is(what, chain):
    what = what.strip()
    try:
        return int(what)
    except ValueError:
        pass

    p = chain[what]
    
    if what not in result:
        if len(p) == 1:
            res =  what_is(p[0], chain)
        elif p[0] == "NOT":
            res = ~ what_is(p[1], chain) & 0xffff # 16 bit unsigned
        elif p[1] == "AND":
            res = what_is(p[0], chain) & what_is(p[2], chain)
        elif p[1] == "OR":
            res = what_is(p[0], chain) | what_is(p[2], chain)
        elif p[1] == "RSHIFT":
            res = what_is(p[0], chain) >> what_is(p[2], chain)
        elif p[1] == "LSHIFT":
            res = what_is(p[0], chain) << what_is(p[2], chain)
        else:
            raise f"Unkonw op: {p}"
        result[what] = res
    
    return result[what]

ops = open("input.txt").read().strip().split("\n")

chain = {}
for op in ops:
    x, y = op.split("->")
    chain[y.strip()] = x.strip().split(" ")

a = what_is("a", chain)

print(a)

chain["b"] = ["16076"]
result = {}

re_a = what_is("a", chain)
print(re_a)
