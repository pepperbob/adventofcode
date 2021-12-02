import re

ticker = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}

data = open("input.txt").read().splitlines()

sues = []
names =  []
for d in data:
    sue = {}
    dd = d.split(":", 1)
    sue['name'] = dd[0]
    tempstuff = [{a[0]: int(a[1])} for a in [i.strip().split(":") for i in dd[1].split(",")]]
    
    sue['stuff'] = {}
    for x in tempstuff:
        sue['stuff'] = {**sue['stuff'], **x}
    
    sues.append(sue)
    names.append(sue['name'])

for s in sues:
    stuff = s['stuff']
    for k in ticker:
        if k in stuff:
            r = False
            if k in ['cats', 'trees']:
                r = ticker[k] > s['stuff'][k]
            elif k in ['pomeranians', 'goldfish']:
                r = ticker[k] <= s['stuff'][k]
            else:
                r = ticker[k] != s['stuff'][k]
            
            if r and s['name'] in names:
                names.remove(s['name'])

print("Gift given by:")
print(names)