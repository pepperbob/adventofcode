
# 97  = a
# 122 = z

def increment(x):
    xx = list(reversed(x))
    l = 0
    while(True):
        if(l > len(xx)-1):
            xx.append("a")
            break

        curr = xx[l]
        if curr == "z":
            xx[l] = "a"
            l += 1
        else:
            xx[l]=chr(ord(curr)+1)
            break
    
    return "".join(list(reversed(xx)))

input = "vzbxkghb"
for x in range(0, 2600000):
    input = increment(input)
    print(input)
