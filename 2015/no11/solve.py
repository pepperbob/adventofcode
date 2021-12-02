
all_abc = [chr(i) for i in range(97,123)]

nots = ["i","o","l"]
dobles = []
for a in all_abc:
    dobles.append(f"{a}{a}")

musts = []
rest_abc = all_abc
while(len(rest_abc)>2):
    musts.append(rest_abc[:3])
    rest_abc = rest_abc[1:]
musts = ["".join(a) for a in musts]

def is_valid(s):
    if any(i in s for i in nots):
        return False
    elif not any(a in s for a in musts):
        return False
    elif len([a for a in dobles if a in s])<2:
        return False        
    return True

def inc_char(ch):
    x = all_abc.index(ch)
    nidx = 0 if x == 25 else x + 1 
    return (all_abc[nidx], nidx==0)

def inc2(x):
    inced = ""
    cont = True
    for s in reversed(x):
        if(not cont):
            inced = s + inced
        else:
            new_c,cont = inc_char(s)
            inced = new_c + inced
    return inced

input = "vzbxxyzz"

valid = False
while(not valid):
    input = inc2(input)
    valid = is_valid(input)
    print(f"{input} = {valid}")
    
