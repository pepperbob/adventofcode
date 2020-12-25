programm = open("input.txt").read().splitlines()

stack = []
for i in programm:
    (op, val) = i.split(" ")
    stack.append((op, int(val)))

accumulator = 0
ptr = 0

maxPtr = len(stack)
ptrDone = []

while(ptr < maxPtr):
    op = stack[ptr]
    if(ptr in ptrDone):
        print(f"Loop Detected: {ptrDone}")
        break

    ptrDone.append(ptr)

    print(f"Operation: {op}")
    if(op[0] == "jmp"):
        ptr += op[1]
        continue
    elif(op[0] == "acc"):
        accumulator = accumulator + op[1]
        ptr = ptr + 1
    else:
        ptr = ptr + 1
    
    
print(f"accumulator={accumulator}")

