class TopItemsList:

    def __init__(self, top = 3, absoluteMin = 0) -> None:
        self.currentMin = absoluteMin
        self.items = [absoluteMin]*top

    def append(self, item):
        if item < self.currentMin:
            return
        
        self.items.remove(self.currentMin)
        self.items.append(item)
        self.currentMin = min(self.items)

    def __iter__(self):
        return self.items.__iter__()


calories = TopItemsList()
curr = 0
with open("input", "r") as f:
    for i in f:
        i = i.strip()
        if i == "":
            calories.append(curr)
            curr = 0

            continue
        curr += int(i)

print(f"Most Calories: {max(calories)}")
print(f"Top 3: {sum(calories)}")