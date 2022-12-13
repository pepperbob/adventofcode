
def assureLists(left, right):
    return left if type(left) == list else [left], right if type(right) == list else [right]

def itemInOrder(left, right):
    if left == right:
        return None
    return left < right

def inOrder(left, right):
    if type(left) == int and type(right) == int:
        return itemInOrder(left, right)

    listLeft, listRight = assureLists(left, right)
    minLen = min(len(listLeft), len(listRight))

    isInOrder = None
    for i in range(minLen):
        isInOrder = inOrder(listLeft[i], listRight[i])
        if isInOrder is not None:
            return isInOrder
    
    if len(listLeft) < len(listRight):
        return True
    if len(listRight) < len(listLeft):
        return False

    return None

# read input
input = [list(map(lambda a: eval(a), x.split("\n"))) for x in open("input", "r").read().split("\n\n")]

# Part 1 - find sorted pairs
result = [(i, inOrder(*x)) for i, x in enumerate(input, 1)]

sumOfIndexesOfPairsInOrder = sum([y[0] for y in result if y[1] == True])
print(f"Sum of indexes of pairs in order: {sumOfIndexesOfPairsInOrder}")

# Part 2 - sort everything
dividerPackets = ([[2]], [[6]])

# flatten and add divider packets
all = [y for x in input for y in x]
all += dividerPackets

# bubble sort time!
goon = True
while goon:
    goon = False
    for indexLeft, indexRight in [(r-1, r) for r in range(1, len(all))]:
        left, right = all[indexLeft], all[indexRight]
        sorted = inOrder(left, right)
        
        if sorted is None or sorted == True:
            continue
        else:
            all[indexLeft] = right
            all[indexRight] = left
            goon = True

# index stuff and filter Divider Packets
indexedDividerPackts = [r for r in [(i, x) for i, x in enumerate(all, 1)] if r[1] in dividerPackets]

p1, p2 = indexedDividerPackts
decoderKey = p1[0]*p2[0]
print(f"Decoder Key is {decoderKey}")
