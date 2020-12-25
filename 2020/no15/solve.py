
start = [2,0,1,7,4,14,18]
#start = [0,3,6]
spokend = dict()

for idx, s in enumerate(start):
    spokend[s] = (idx+1, 0)
    print(f"{idx+1}: {s}")

last = start[-1]
turn = len(start)
while(turn < 30000000):
    turn += 1
    
    if(spokend[last][1] == 0):
        spokend[0] = (turn, spokend[0][0])
        last = 0
    else:
        nxt = spokend[last][0] - spokend[last][1]

        lastturn = 0 if nxt not in spokend else spokend[nxt][0]
        spokend[nxt] = (turn, lastturn)
        last = nxt
    
print(f"{turn}: {last}")
