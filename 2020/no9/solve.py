import itertools

def possibilities(encode):
    possibles = [i for i in list(itertools.product(encode, encode)) if i[0] != i[1]]
    return list(map(lambda i: int(i[0])+int(i[1]), possibles)) 

xmas = open("input.txt").read().splitlines()

preamble = 25

print(xmas)
for idx, curr in enumerate(range(preamble, len(xmas))):
    encode = possibilities(xmas[idx:idx+preamble])
    code = xmas[curr]
    if(int(code) not in encode):
        print(f"unexpected: {code}")
