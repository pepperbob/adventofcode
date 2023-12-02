# Good Luck

digitsmap = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def concat_first_last_digit(calibration_values, solve_part_two=False):
    res = []
    for line in calibration_values:
        t = []
        for i, d in enumerate(line):
            ## for part 1
            if d.isdigit():
                t.append(int(d))
                continue
            
            ## for part 2
            if solve_part_two:
                for x in digitsmap:
                    if list(x) == list(line)[i:i+len(x)]:
                        t.append(digitsmap[x])

        res.append(f"{t[0]}{t[-1]}")
    return res


input = open("01/input.txt").read().splitlines()

res1 = sum([int(x) for x in concat_first_last_digit(input)])
res2 = sum([int(x) for x in concat_first_last_digit(input, solve_part_two=True)])
print(f"1* Result: {res1}")
print(f"2* Result: {res2}")
