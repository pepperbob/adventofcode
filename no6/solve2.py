
group_answer = [[]]

with open("input.txt") as f:
    for l in f.read().splitlines():
        if (not l):
            group_answer.insert(0, [])
        else:
            group_answer[0].append(list(l))

intersected = []
for group in group_answer:
    for idx, answer in enumerate(group):
        if(idx == 0):
            intersected.append(answer)
        else:
            intersected[-1] = list(set(intersected[-1]) & set(answer))

counts = []
for inter in intersected:
    counts.append(len(inter))


print(f"result is {sum(counts)}")