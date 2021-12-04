
metrics = open("input.txt").read().split()

def most_char(arr, pos):
    ones = 0
    zero = 0
    for s in arr:
        if s[pos] == "1":
            ones += 1
        else:
            zero += 1

    return "1" if ones >= zero else "0"

def oppositve(zero_one):
    return "0" if zero_one == "1" else "1"

def filter(list, pos, expect):
    filtered = []
    for m in list:
        if m[pos] == expect:
            filtered.append(m)
    return filtered

filtered_oxy = metrics

for pos in range(0, len(metrics[0])):
    filter_for = most_char(filtered_oxy, pos)
    filtered_oxy = filter(filtered_oxy, pos, filter_for)
    if len(filtered_oxy) == 1:
        break

filtered_scrub = metrics
for pos in range(0, len(metrics[0])):
    filter_for = oppositve(most_char(filtered_scrub, pos))
    filtered_scrub = filter(filtered_scrub, pos, filter_for)
    if len(filtered_scrub) == 1:
        break

print(filtered_oxy)
print(filtered_scrub)

print(int(filtered_oxy[0],2)*int(filtered_scrub[0],2))