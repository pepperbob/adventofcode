import hashlib
import itertools

input = "wtnhxymk"

hh = []
for x in itertools.count(0, 1):
    h  = hashlib.md5(f"{input}{x}".encode("utf8")).hexdigest()
    if h.startswith("00000"):
       hh.append(h[5])
       print(h)
    if len(hh) == 8:
        break
print("".join(hh))
