
data = open("input-test").read().strip() + "0"
disk = []
nodes = {}
for i, b in enumerate(zip(data[::2], data[1::2])):
    fsize = int(b[0])
    space = int(b[1])
    start = len(disk)
    disk.extend([i]*fsize)
    disk.extend([None]*space)

    # store start-index, end-index, size, space
    nodes[i] = [start, start+fsize, fsize, space]

print(nodes)
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

for i in range(DISK_SIZE):
    if disk[i] is None:
        xx = find_last(disk, i)
        if xx is None:
            break

        disk[i] = disk[xx]
        disk[xx] = None

solution1 = 0
for i, c in enumerate(disk):
    if c is None:
        break
    solution1 += i * c

print("Solution 1", solution1)

def find_free_space(nnodes, ofsize, stop):
    print("Looking for ", ofsize, "space in", nnodes)
    for i, k in enumerate(nnodes.values()):
        if i >= stop:
            break

        if k[3] >= ofsize:
            print("Found", ofsize,"in",k)
            return i 

    return None

def print_disk(dsk):
    print("".join(["." if i is None else str(i) for i in dsk]))

for i in range(max(nodes.keys()), -1, -1):
    start, end, size, free = nodes[i]
    block_with_free_idx = find_free_space(nodes, size, i) 

    if block_with_free_idx is None:
        print("Skipping", nodes[i])
        continue

    for ii, m in enumerate(range(start, end)):
        target_idx = nodes[block_with_free_idx][1]+ii
        disk[target_idx] = disk[m]
        disk[m] = None
        # insert stuff

    nodes[block_with_free_idx][3] -= size
    print_disk(disk) 
    input("..") 



