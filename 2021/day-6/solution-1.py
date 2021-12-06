

fish = [int(x) for x in open("input.txt").readline().split(",")]

days = 80

while days > 0:
    print(f"---- DAY {days} ----")
    days -= 1
    
    new_fish = []
    for i, f in enumerate(fish):
        if f == 0:
            new_fish.append(8)
            fish[i] = 6
        else:
            fish[i] = f - 1
    fish += new_fish

    print(len(fish))