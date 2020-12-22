#!/usr/bin/env python
import fileinput
from collections import defaultdict

#fn="input_test.txt"
fn="input.txt"

ops = open(fn).read().strip().replace("contains ", "").split("\n")

# parse lits to allergene -> ingredient

foods = {}
for idx, op in enumerate(ops):
    a = False
    ingre = []
    aller = []

    for o in op.split(" "):
        if o[0] == "(":
            a = True
            aller.append(o[1:].replace(")", "").replace(",", ""))
        elif o[-1] == ")":
            a = False
            aller.append(o[:-1].replace("(", ""))
        elif a:
            aller.append(o.replace(",", ""))
        else:
            ingre.append(o)
    
    foods[idx] = (ingre, aller) 

# build all known ingredients:
all_i = [foods[i][0] for i in foods]
all_i = [item for sublist in all_i for item in sublist]

all_a = defaultdict(lambda: [])
for f in foods:
    for a in foods[f][1]:
        all_a[a] += foods[f][0]

intersected = all_a
# intersect known ingredient-combinations per allergene
for f in foods.values():
    for a in f[1]:
        intersected[a] = list(set(intersected[a]) & set(f[0])) 
 
allergene_ingre = [intersected[i] for i in intersected]
allergene_ingre = [i for sublist in allergene_ingre for i in sublist]

no_allergene_ingre = set([f for f in all_i if f not in allergene_ingre])

acc=0
for i in no_allergene_ingre:
    for o in foods:
        occ = foods[o][0].count(i)
        acc += occ

print(f"Appearances: {acc}")
print(f"No Allergenes: {len(no_allergene_ingre)}")

    
### part 2
# ... solved it manually :/
"""
dairy=['vfvvnm']
eggs=['bvgm']
fish=['rdksxt']
nuts=['xknb']
peanuts=['hxntcz']
sesame=['bktzrz']
soy=['srzqtccv']
wheat=['gbtmdb']

vfvvnm,bvgm,rdksxt,xknb,hxntcz,bktzrz,srzqtccv,gbtmdb
"""