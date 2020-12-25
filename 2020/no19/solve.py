#!/usr/bin/env python
import fileinput
import numpy as np
import sys


def expand(pattern, rules, curr = [""], depth=0):
    subpattern = list(map(lambda s: s.strip().replace("\"", ""), pattern.split("|")))

    tcurr = []
    
    for sub in subpattern:
        
        # copy current
        scurr = list(curr)
        for c in list(map(lambda s: s.strip(), sub.split(" "))):
            if c[0] in list("0123456789"):
                # expand here
                print(f"{'.'*depth} recursion to resolve {c} from {sub}")
                scurr = expand(rules[int(c)], rules, scurr, depth+1)
            else:
                # add here
                for cidx, ccurr in enumerate(scurr):
                    scurr[cidx]= ccurr + c
        
        # collect stuff again
        tcurr.extend(scurr)
    
    return tcurr

ops = [s for s in list(map(lambda  s: s.strip(), fileinput.input())) if len(s) > 1]

pre_rules = []
payload = []
for op in ops:
    if(op[0] in list("0123456789")):
        pre_rules.append(op)
    else:
        payload.append(op)

rules=[""]*len(pre_rules)
for pre in pre_rules:
    ab,b = pre.split(":")
    rules[int(ab)] = b.strip()

combinations = expand(rules[0], rules)
ok = []
for p in payload:
    if(p in combinations):
        ok.append(p)

print(len(ok))

