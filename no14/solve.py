#!/usr/bin/env python
import fileinput
import operator

def bin(i, s):
    return list(("{0:0"+str(s)+"b}").format(i))

def setmask(op):
    return op.split(" = ")[1]

def writemem(mem, mask, op):
    l, r = op.split(" = ")
    mem[l] = comb(int(r), mask)

def comb(i, mask):
    bini = bin(i, 36)
    c = []
    for a, b in zip(bini, list(mask)):
        c.append(a if b == "X" else b)
    return "".join(c)

ops = list(map(lambda  s: s.strip(), fileinput.input()))

mask = None
mem = dict()
for op in ops:
    if(op.startswith("mask")):
        mask=setmask(op)
    else:
        writemem(mem, mask, op)

xx = [int(mem[i], 2) for i in mem.keys()]
print(sum(xx))

def explodeaddr(addr, rawmask):
    addrmasked = ""
    for a,b in zip(list(addr), list(rawmask)):
        addrmasked += a if b == "0" else b
    
    print(f"{addr} | {rawmask} > {addrmasked}")
    r = addrmasked.count("X")
    masks = []

    for i in range(int("1"*r, 2)+1):
        mask = addrmasked
        for x in bin(i, r):
            mask = mask.replace("X", x, 1)
        masks.append(mask)

    print(masks)
    print("\n\n")
    return masks

def writemems(mem, mask, op):
    l, r = op.split(" = ")
    iaddr = int(l.replace("mem[", "").replace("]", ""))
    addr = "".join(bin(iaddr, 36))

    for m in explodeaddr(addr, mask):
        mem[m] = int(r)

mem = dict()
mask = None
for op in ops:
    if(op.startswith("mask")):
        mask=setmask(op)
    else:
        writemems(mem, mask, op)

yy = [mem[i] for i in mem.keys()]
print(sum(yy))