import hashlib 

input = "ckczppom"

i = 0
hash = ""
while True:
    hash = hashlib.md5(f"{input}{i}".encode('utf-8')) 
    if hash.hexdigest().startswith("000000"):
        break

    i += 1

print(f"{i} = {hash.hexdigest()}")