import re

def transpose(matrix):
    """
    Transpose Matrix 90° right
    """
    return [[matrix[j][i] for j in range(len(matrix)) if matrix[j][i] != ""] for i in range(len(matrix[0]))]

def readInput(inputLines):
    mode_op = False
    stacks = []
    operations = []
    n=4
    for line in inputLines:
        if line == "\n":
            mode_op = True
            continue

        if mode_op == True:
            operations.append(line)
        else:
            chunks = [line[i:i+n].strip() for i in range(0, len(line), n)]
            stacks.append(chunks)
    return (transpose(stacks), operations)


# Regex to parse commands
command = r"move (\d+) from (\d+) to (\d+)"
input = open("input", "r").readlines()

(stacks, operations) = readInput(input)

# part 1
for op in operations:
    (cnt, source, target) = re.match(command, op).groups()
    sourceStack = stacks[int(source)-1]
    targetStack = stacks[int(target)-1]
    for i in range(int(cnt)):
        targetStack.insert(0, sourceStack.pop(0))

cratesOnTopOfStack = "".join([i[0].replace("[", "").replace("]", "") for i in stacks])

print(f"Crates on top with Mover 9000: {cratesOnTopOfStack}")
del stacks

# part 2
(stacks, operations) = readInput(input)

for op in operations:
    (cnt, source, target) = re.match(command, op).groups()
    sourceStack = stacks[int(source)-1]
    targetStack = stacks[int(target)-1]
    stackToMove = []
    for i in range(int(cnt)):
        stackToMove.append(sourceStack.pop(0))


    print(op.strip())
    for i in reversed(stackToMove):
        targetStack.insert(0, i)

cratesOnTopOfStack = "".join([i[0].replace("[", "").replace("]", "") for i in stacks])
print(f"Crates on top with Mover 9001: {cratesOnTopOfStack}")
