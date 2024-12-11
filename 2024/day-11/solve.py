data = list(map(int, open("input").read().strip().split(" ")))

def split_in_2(no):
    stno = str(no)
    lstr = len(stno)//2
    return list(map(int, (stno[0:lstr], stno[lstr:])))

def multiply_with_2024(no):
    return no*2024

def map_to_1(no):
    return 1

def process(dat):
    mapped = []
    for i in dat:
        if i == 0:
            mapped.append(map_to_1(i))
        elif len(str(i))%2 == 0:
            r = split_in_2(i)
            # print("Split", i, ":", r)
            mapped.extend(r)
        else:
            mapped.append(multiply_with_2024(i))
    return mapped


round = 0
while round < 25:
    data = process(data)
    round += 1

print(len(data))
