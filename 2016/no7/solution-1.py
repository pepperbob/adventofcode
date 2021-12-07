import re


ips = [re.findall(r"\[?[a-z]+\]?", x) for x in open("input.txt").readlines()]

def qualifies(code):
    # -1: does not support, 1: support, 0: dunno
    invert = False
    if code[0] == "[":
        invert = True
    
    for a,b,c,d in zip(code, code[1:], code[2:], code[3:]):
        # abba
        if a == d and b == c and a != b:
            return -1 if invert is True else 1
    
    return 0

no = 0
for ip in ips:
    counts = False
    for i in ip:
        test = qualifies(i)
        if test == -1:
            # done here
            counts = False
            break
        
        if test == 1:
            counts = True
    if counts:
        no += 1

print(no)