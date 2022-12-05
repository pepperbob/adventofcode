import re

def transpose(matrix):
    """
    Transpose Matrix 90° (clockwise)
    """
    return [[matrix[j][i] for j in range(len(matrix)) if matrix[j][i] != ""] for i in range(len(matrix[0]))]

def readInput():
    """
    Parse the input lines to stacks and operations, transpose stacks for easier handling
    """
    inputLines = open("input", "r").readlines()

    mode_op = False
    stacks = []
    operations = []
    n=4
    for line in inputLines:
        if line == "\n":
            mode_op = True
            continue
        
        if mode_op == True:
            operations.append(line.strip())
        else:
            chunks = [line[i:i+n].strip().replace("[", "").replace("]", "") for i in range(0, len(line), n)]
            stacks.append(chunks)
    return (transpose(stacks), operations)

# Regex to parse commands
command = r"move (\d+) from (\d+) to (\d+)"

# part 1

(stacks, operations) = readInput()
for op in operations:
    (cnt, source, target) = re.match(command, op).groups()
    sourceStack = stacks[int(source)-1]
    targetStack = stacks[int(target)-1]
    for i in range(int(cnt)):
        targetStack.insert(0, sourceStack.pop(0))

cratesOnTopOfStack = "".join([i[0] for i in stacks])

print(f"Crates on top with Mover 9000: {cratesOnTopOfStack}")

del stacks
del operations
del cratesOnTopOfStack

# part 2
(stacks, operations) = readInput(input)
for op in operations:
    (cnt, source, target) = re.match(command, op).groups()
    sourceStack = stacks[int(source)-1]
    targetStack = stacks[int(target)-1]
    cratesToMove = []
    for i in range(int(cnt)):
        cratesToMove.append(sourceStack.pop(0))
    
    stacks[int(target)-1] = cratesToMove + targetStack

cratesOnTopOfStack = "".join([i[0] for i in stacks])
print(f"Crates on top with Mover 9001: {cratesOnTopOfStack}")
