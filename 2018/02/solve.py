
input = open("input", "r").read().splitlines()

two = 0
three = 0
for i in input:
    ii = set(i)

    hastwo = False
    hasthree = False
    for si in ii:

        ci = i.count(si)
        if ci == 2:
            hastwo = True
        elif ci == 3:
            hasthree = True
        
        if hastwo and hasthree:
            break

    if hastwo:
        two +=  1
    
    if hasthree:
        three += 1

print(two*three)