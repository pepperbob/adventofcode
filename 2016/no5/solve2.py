import hashlib
import itertools

input = "wtnhxymk"

valids = [str(x) for x in range(0,8)]
hh = ["_"]*8

for x in itertools.count(0, 1):
    h  = hashlib.md5(f"{input}{x}".encode("utf8")).hexdigest()
    if h.startswith("00000") and h[5] in valids and hh[int(h[5])] == "_":
        hh[int(h[5])] = h[6] 
        out = "".join(hh)
        print('Guessing... [%s]\r'%out, end="")
    
    if len([x for x in hh if x != "_"]) == 8:
        break

print("".join(hh))
