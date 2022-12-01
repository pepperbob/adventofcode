

theList = open("input", "r").readlines()

most = 0
curr = 0
calories = []
for i in theList:
    ii = i.strip()
    if ii == "":
        most = curr if curr >= most else most
        calories.append(curr)
        curr = 0

        continue

    curr += int(ii)

print(f"Most Calories: {most}")

top3 = list(reversed(sorted(calories)))[0:3]
print(f"Top 3: {sum(top3)}")