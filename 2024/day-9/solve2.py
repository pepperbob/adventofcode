
data = open("input").read().strip() + "0"
disk = []
nodes = {} # keep track of file blocks
for i, b in enumerate(zip(data[::2], data[1::2])):
    fsize = int(b[0])
    space = int(b[1])
    start = len(disk)
    disk.extend([i]*fsize)
    disk.extend([None]*space)

    # store block end, space, file start, file size
    nodes[i] = [start+fsize, space, start, fsize]

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
        if k[1] >= ofsize:
            return i 
    return None

# iterate from the back
for i in range(max(nodes.keys()), -1, -1):

    fstart = nodes[i][2] 
    filesize = nodes[i][3] 

    # find file index with enough space to keep the current file
    block_with_free_idx = find_free_space(nodes, filesize, i) 

    if block_with_free_idx is None:
        # no space, skip this file
        continue
   
    # copy file to free space
    for ii, m in enumerate(range(fstart, fstart+filesize)):
        # append to the end
        target_idx = nodes[block_with_free_idx][0]+ii
        disk[target_idx] = disk[m]
        disk[m] = None

    # update occupied end position
    nodes[block_with_free_idx][0] += filesize

    # uppdate space left in block
    nodes[block_with_free_idx][1] -= filesize

print("Solution 2", calc_checksum(disk))

