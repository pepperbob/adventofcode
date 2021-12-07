import re

ips = [re.findall(r"\[?[a-z]+\]?", x) for x in open("input.txt").readlines()]

def hasMatchingBAB(ip, aba):
    babSource = "".join([i for i in ip if "[" in i])
    for a in aba:
        if a[1]+a[0]+a[1] in babSource:
            return True
    return False

def extractABA(ip):
    aba = set()
    for i in ip:
        if "[" in i:
            continue

        for a,b,c in zip(i, i[1:], i[2:]):
            if a == c and a != b:
                aba.add(a+b+c)

    return aba

no = 0
for ip in ips:
    aba = extractABA(ip)
    if hasMatchingBAB(ip, aba):
        no += 1

print(no)