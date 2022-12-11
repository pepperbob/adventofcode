CRT_WIDTH = 40
CRT_HEIGHT = 6

def checkCycle(cycle, x, iss, crt):
    crtIndex = cycle-1
    offset = (crtIndex//CRT_WIDTH)*CRT_WIDTH
    sprite=(x+offset-1, x+offset, x+offset+1)
    if crtIndex in sprite:
        crt[crtIndex]="#"
    
    if cycle in (20, 60, 100, 140, 180, 220):
        iss.append(cycle * x)

programm = open("input", "r").read().splitlines()

cycle = 1
valueOf_x = 1
singal_stengths = []
crt = ["."]*(CRT_WIDTH*CRT_HEIGHT)

for instruction in programm:

    checkCycle(cycle, valueOf_x, singal_stengths, crt)
    cycle += 1
    
    if instruction != "noop":
        checkCycle(cycle, valueOf_x, singal_stengths, crt)
        cycle +=1
        valueOf_x += int(instruction.split(" ")[1])

print(f"Part 1: sum of signal strength: {sum(singal_stengths)}")

print(f"Part 2: Render CRT")
for i in range(1, len(crt)+1):
    print(crt[i-1], end="")
    if(i%CRT_WIDTH == 0):
        print()