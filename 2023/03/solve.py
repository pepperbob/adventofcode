import math

directions = [(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(1,1),(1,-1),(-1,1)]

input = [list(x) for x  in open("03/input").read().split()]

symbols = lambda x: not x.isdigit() and not x == "."
gears = lambda x: x == "*"

def detect_part(pos, arr, strat = symbols):
    x, y = pos
    all_pos = [(a+x,b+y) for a,b in directions]
    all_pos = [(a,b) for a,b in all_pos if a>=0 and b>=0 and a<len(arr) and b<len(arr[0])]
    for p in all_pos:
        c = arr[p[0]][p[1]]
        if strat(c):
            return (True, p)

    return (False, None)

res1 = 0
gears_dict = dict()

for x, row in enumerate(input):
    curr_digit = []
    is_part = False
    gear_pos = None

    for y, c in enumerate(row):
        if c.isdigit():

            curr_digit.append(c)
            
            # detect if symbol
            linked_to_part, _ = detect_part((x,y), input)
            
            if linked_to_part:
                is_part = True

            # detect if attached to gear (part 2)
            linked_to_gear, linked_gear_pos = detect_part((x,y), input, gears)
            if linked_to_gear:
                gear_pos = linked_gear_pos

        if (y+1 == len(row) or not c.isdigit()) and len(curr_digit) > 0:
            parsed_digit = int("".join(curr_digit))
            if is_part:
                res1 += parsed_digit
            
            if gear_pos is not None:
                if gear_pos in gears_dict:
                    gears_dict[gear_pos].append(parsed_digit)
                else:
                    gears_dict[gear_pos] = [parsed_digit]

            is_part = False
            curr_digit = []
            gear_pos = None

print(f"1* Result: {res1}")

res2 = sum([math.prod(x) for x in gears_dict.values() if len(x)>1])
print(f"2* Result: {res2}")