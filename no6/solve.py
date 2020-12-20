
group_answer = [[]]

with open("input.txt") as f:
    for l in f.read().splitlines():
        group_answer[0].extend(list(l))
        if (not l):
            group_answer.insert(0, [])

answers = []
for answer in group_answer:
    answers.append(len(set(answer)))

print(f"Part one: {sum(answers)}")

print(group_answer)