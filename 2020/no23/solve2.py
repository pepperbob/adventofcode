
input = "562893147"
#input = "123456789"

def printc(cccs, c):
    x = str(c)
    next = c
    while True:
        a = cccs[next]
        if str(a) in x:
            x += str(a)
            break
        x += str(a)
        next = a

    print(x)


# setup [number] -> successor
start_cups = list(map(lambda x: int(x), list(input))) + list(range(10, 1000001))
cups = [0]*(len(start_cups)+1)

for a, b in zip(start_cups, start_cups[1:]):
    cups[a] = b
cups[b] = 5

start_cups = None

curr = int(input[0])
for i in range(10_000_000):

    # re-arrgange:
    r1 = cups[curr]
    r2 = cups[r1]
    r3 = cups[r2]

    dest = curr - 1 if curr > 1 else len(cups) - 1
    while dest in (r1, r2, r3):
        dest = dest - 1 if dest > 1 else len(cups) - 1
    
    # re-link
    #print(f"{curr}->{cups[r3]}")
    cups[curr] = cups[r3]

    tmp = cups[dest]
    #print(f"{dest}->{r1}")
    cups[dest] = r1
    #print(f"{r3}->{tmp}")
    cups[r3] = tmp
    curr = cups[curr]

r1 = 1
r2 = cups[r1]
r3 = cups[r2]

res = r2*r3

print((r1, r2, r3, res))