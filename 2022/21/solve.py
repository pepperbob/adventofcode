import re

ii = {x : v for x,v in [x.split(":") for x in open("input", "r").read().strip().splitlines()]}

def calc(name, all):
    value = all[name].strip()
    if re.match(r"\d", value):
        return int(value)
    else:
        left, op, right = value.split(" ")
        lnr = calc(left, all)
        rnr = calc(right, all)
        return int(eval(f"{lnr}{op}{rnr}"))

rootYells = calc("root", ii)

print(f"Monkey root yells {rootYells}")


def makeTree(name, all):
    if name == "humn":
        return "humn"
    value = all[name].strip()
    if re.match(r"\d", value):
        return int(value)
    else:
        left, op, right = value.split(" ")
        lnr = makeTree(left, all)
        rnr = makeTree(right, all)
        
        if name == "root":
            return (lnr, rnr)
            
        return (f"({lnr}{op}{rnr})")

# make expression tree
leftright = makeTree("root", ii)

# left is with humn
left, right = leftright if "humn" in leftright[0] else (leftright[1], leftright[0])

# sure, eval right
right = eval(right)


diff = 1
humn = 0
latestTooBig = 0
iter = 0

# guess humn must be >0
while True:

    iter += 1

    # humn is left, so replace it with actual value
    ll = eval(left.replace("humn", f"{humn}"))

    # this whole loop assumes left > right if humn = 0
    # and we're looking for humn > 0

    # every x iterations double diff to hit upper bound faster
    if (iter % 5):
        diff *= 2

    if ll > right:
        # store latest humn where left > right
        latestTooBig = humn
    
    elif ll < right:
        # too much humn: reset to latest "left > right" and restart diff
        humn = latestTooBig
        diff = 1
    else:
        print(f"Human must yell {humn}")
        break

    # add the diff
    humn += diff
    
        
