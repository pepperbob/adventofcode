#            1,  1
# 3+3+1+1 =  8,  9
# 5+5+3+3 = 16, 25
# 7+7+5+5 = 24, 49
# 9+9+7+7 = 32, 81
# 11+11+9+9 = ...

"""
7 
   17  16  15  14  13
   18   5   4   3  12
   19   6   1   2  11
   20   7   8   9  10
   21  22  23  24  25 
                     
"""

needle = 277678

# calc one diagonal only (1,1), (2,2), ), (3,3), ...
x,y = 3,1
# pos = [step, pos, value at pos]
pos = [[0, (0,0), 1], [1, (1,1), x+x+y+y + 1]]
i = pos[-1][0]
while(True):
    i += 1
    latest = pos[-1]
    # x,y increase by 2 per iteration
    valAtPos = latest[2] + (2*(x+2*(i-1)))+(2*(y+2*(i-1)))
    c = latest[1]
    pos.append([i, (c[0]+1,c[0]+1), valAtPos])

    if valAtPos > needle:
        break

beforelast = pos[-2]
print(beforelast)
last = pos[-1]
print(last)
print(f"Needle: {needle}")
diff_pos_needle = last[2]-needle # we are lucky i guess
print(f"Diff to needle: {diff_pos_needle}")
pos_needle = (last[1][0], last[1][1]-diff_pos_needle) # really lucky... does not work with every input
print(f"Pos of Needle: {pos_needle}")
print(f"1* Distance to (0,0) = {sum(pos_needle)}")

# https://oeis.org/ OMG
print(f"2* See https://oeis.org/A141481 - crazy, thx reddit")