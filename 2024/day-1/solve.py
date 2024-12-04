
data = open("input").read().splitlines()

first_col = sorted([int(x.split(" ")[0]) for x in data])
last_col = sorted([int(x.split(" ")[-1]) for x in data])
distances = [abs(x-y) for x, y in zip(first_col, last_col)]
    
print(sum(distances))

similarities = sum([i * last_col.count(i) for i in first_col])

print(similarities)