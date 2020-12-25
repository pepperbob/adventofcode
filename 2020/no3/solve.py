import re

lines = []
with open("input.txt", "r") as f:
    for l in f.readlines():
        lines.append(list(l.replace("\n", "")))

def slopethrough(right, down, lines):
    x=0
    y=0
    ymax = len(lines[0])
    path = []
    while(x < len(lines)-down):
        x += down
        y = y + right if y < ymax-right else (y+right-ymax)
        
        path.append(lines[x][y])
    
    return path


paths = [slopethrough(1,1,lines), slopethrough(3,1,lines), 
    slopethrough(5,1,lines), slopethrough(7,1,lines), slopethrough(1,2,lines)]

trees = map(lambda tree: len(tree), 
    map(lambda path: [p for p in path if p == "#"], paths))

prod = 1
for p in trees:
    prod *= p

print(prod)
