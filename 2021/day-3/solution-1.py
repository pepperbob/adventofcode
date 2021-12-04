

metrics = open("input.txt").read().split()

sum_per_col = [0]*len(metrics[0])
gamma_indicator = len(metrics)/2

for m in metrics:
    for i, s in enumerate(list(m)):
        sum_per_col[i] += int(s)

# OMG
gammas = "".join(["1" if x >= gamma_indicator else "0" for x in sum_per_col])
epsilon = "".join(["0" if x == "1" else "1" for x in list(gammas)])

print(int(gammas,2)*int(epsilon, 2))

