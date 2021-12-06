import collections

singleFish = [int(x) for x in open("input.txt").readline().split(",")]

fish = collections.defaultdict(lambda: 0)
fish.update(collections.Counter(singleFish))

days = 256

while days > 0:
    print(f"---- DAY {days} ----")
    days -= 1

    new_fish = collections.defaultdict(lambda: 0)
    for age in fish.keys():
        if age == 0:
            new_fish[8] = new_fish[8] + fish[age]
            new_fish[6] = new_fish[6] + fish[age]
        else:
            new_fish[age-1] = new_fish[age-1] + fish[age]
    
    fish = new_fish
    print(sum(fish.values()))