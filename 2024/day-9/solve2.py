
data = open("input").read().strip() + "0"
disk = []
nodes = {}
for i, b in enumerate(zip(data[::2], data[1::2])):
    fsize = int(b[0])
    space = int(b[1])
    start = len(disk)
    disk.extend([i]*fsize)
    disk.extend([None]*space)

    # store start-index, end-index, size, space, file start, file end
    nodes[i] = [start, start+fsize, fsize, space, start, start+fsize]

DISK_SIZE = len(disk)
USED_SPACE = len([x for x in disk if x is not None])
FREE_SPACE = len([x for x in disk if x is None])

print("Size:", DISK_SIZE, "Used:", USED_SPACE, "Free:", FREE_SPACE)
input("Press Any Key to Defrag")

def find_last(dsk, excluding):
    for i in range(DISK_SIZE-1, excluding, -1):
        if dsk[i] is not None:
            return i
    return None

def calc_checksum(dsk):
    solution = 0
    for i, c in enumerate(disk):
        if c is None:
           continue 
        solution += i * c
    return solution

def find_free_space(nnodes, ofsize, stop):
    for i, k in enumerate(nnodes.values()):
        if i >= stop:
            break

        if k[3] >= ofsize:
            return i 

    return None

def print_disk(dsk):
    print("".join(["." if i is None else str(i) for i in dsk]))

for i in range(max(nodes.keys()), -1, -1):
    start = nodes[i][0]
    end = nodes[i][1]
    size = nodes[i][2]
    fstart = nodes[i][4] 
    fend = nodes[i][5] 

    block_with_free_idx = find_free_space(nodes, fend-fstart, i) 

    if block_with_free_idx is None:
        continue
    
    for ii, m in enumerate(range(fstart, fend)):
        # append to the end
        target_idx = nodes[block_with_free_idx][1]+ii
        disk[target_idx] = disk[m]
        disk[m] = None
        # insert stuff

    # update occupied end position
    nodes[block_with_free_idx][1] += size
    # update free size
    nodes[block_with_free_idx][2] += size-1
    nodes[block_with_free_idx][3] -= size

print("Solution 2", calc_checksum(disk))

