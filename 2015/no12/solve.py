

input = open("input.txt").read().strip()
repl = '{}[]abcdefghijklmnopqrstuvwxyz:\\="'

for r in repl:
    input = input.replace(r, "")

x = [n for n in input.split(",") if len(n)>0]
x = sum(map(int, x))
print(x)