import json

data = None
with open("input.txt") as input:
    data = json.load(input)

all_int = []

def visit_dict(d):
    for k in d:
        visit(d[k])

def visit(d):
    if type(d) is str:
        print("string")
    elif type(d) is dict:
        if "red" not in d.values():
            visit_dict(d)
        else:
            print("Found RED!")
    elif type(d) is list:
        for x in d:
            visit(x)
    elif type(d) is int:
        all_int.append(d)
    else:
        print(type(d))

visit_dict(data)

print(sum(all_int))