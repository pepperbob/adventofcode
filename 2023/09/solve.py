
raw = [list(map(int, x.split(" "))) for x in open("09/input").read().splitlines()]


def gen_row_below(items):
    for a, b in zip(items, items[1:]):
        yield b-a


res1 = []
for x in raw:
    diffs = [x]
    while True:
        below = list(gen_row_below(diffs[-1]))
        diffs.append(below)
        if len(set(below)) == 1 and below[0] == 0:
            break

    # part 2: just reverse everything
    #for i in range(len(diffs)):
    #    diffs[i] = list(reversed(diffs[i]))

    last_items = [l[-1] for l in diffs]

    calc_next_last = last_items[-1]
    for i in range(len(last_items)-1,-1,-1):        
        calc_next_last = last_items[i] + calc_next_last
        # part 2: substract instead
        # calc_next_last = last_items[i] - calc_next_last

        diffs[i].append(calc_next_last)
    
    res1.append(calc_next_last)

print(f"1* Result: {sum(res1)}")
