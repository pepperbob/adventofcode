from scipy.sparse import csr_matrix
import math
from scipy.sparse.csgraph import dijkstra

raw = open("input-test").read().splitlines()
DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]
BOUNDX, BOUNDY = 6+1, 6+1 # 70+1,70+1
BYTES = 1024 
fallen = []

for r in raw:
    x,y = map(lambda x: int(x), r.replace("(", "").replace(")", "").split(","))
    fallen.append((y, x)) # left, top -> top, left

def in_bound(pos):
    x,y = pos
    return x >= 0 and y >= 0 and x < BOUNDX and y < BOUNDY

ADJ_LOOK = {
}
def adj_coordinates(lnode):
    lx, ly = lnode 
    adj_x = lx*BOUNDX+ly
    ADJ_LOOK[adj_x] = lnode

    def inner_adj_coord(rnode):
        rx,ry = rnode 
        adj_y = rx*BOUNDX+ry
        ADJ_LOOK[adj_y] = rnode

        return adj_x, adj_y
    return inner_adj_coord

def to_abs(i):
    iy = i%(BOUNDX)
    # print(str(i), "iy=", str(iy))
    ix = (i-iy)//(BOUNDX*BOUNDY)
    # print("From", str(i), " = ", (ix,iy))
    # input("..")
    return (ix,iy)

def print_mem(path = []):
    for x, X in enumerate(memory):
        for y, Y in enumerate(X):
            if (x,y) in path:
                print("O", end="")
            else:
                print(Y, end="")
        print("")

def get_path(Pr, i, j):
    path = [j]
    k = j
    while Pr[i, k] != -9999:
        path.append(Pr[i, k])
        k = Pr[i, k]
    return path[::-1]

def print_path(Pr):
    the_path = [ADJ_LOOK[x] for x in get_path(Pr, istart, iend)]
    moves = []
    for x in the_path:
        moves.append(x)
        print_mem(moves)
        print("--")
        input("..")

memory = [["."]*BOUNDY for x in range(BOUNDX)]
adj_matrix = [[0]*BOUNDX*BOUNDY for x in range(BOUNDX*BOUNDY)]

istart = 0 
iend = BOUNDX*BOUNDY-1

for x, X in enumerate(memory):
    for y, Y in enumerate(X):
        nexts = [(x+d[0], y+d[1]) for d in DIRECTIONS]
        nexts = [nxt for nxt in nexts if in_bound(nxt)]
        nexts = map(adj_coordinates((x,y)), nexts)

        for n in nexts:
            adj_matrix[n[1]][n[0]] = 1
            adj_matrix[n[0]][n[1]] = 1
print(len(fallen), "Corruptions")

# Corrupt Memory Step by Step:
for i, b in enumerate(fallen):
    x, y = b
    memory[b[0]][b[1]] = "#"

    # build matrix:
    nexts = [(x+d[0], y+d[1]) for d in DIRECTIONS]
    nexts = [nxt for nxt in nexts if in_bound(nxt)]
    # print("Cut off", nexts)
    # print_mem(nexts)
    nexts = map(adj_coordinates(b), nexts)
    # input()

    # print_mem([(x,y)])
    for n in nexts:
        adj_matrix[n[1]][n[0]] = 0
        adj_matrix[n[0]][n[1]] = 0
    
    if i >= 0: # 2980:
        print("Check block", i)
        graph = csr_matrix(adj_matrix)
        D, Pr= dijkstra(csgraph=graph, directed=False, return_predecessors=True)
        # print_path(Pr)
        # input("..")
        dist = D[istart][iend]
        if dist == math.inf:
            print("Cut off with", b)
            break
        else:
            print("ok")


