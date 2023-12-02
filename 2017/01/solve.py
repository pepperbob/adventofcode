
def solveIt(input: str):
    sum = 0
    zipwith = list(input[1:]) + [input[0]]
    for d, dn in zip(input, zipwith):
        if d == dn:
            sum += int(dn)
    return sum

def solveIt2(ii: str):
    sum = 0
    half = int(len(ii)/2)

    input = list(ii)
    zipwith = input[half:] + input[:half]
    for d, dn in zip(input, zipwith):
        if d == dn:
            sum += int(dn)
    return sum

if __name__ == "__main__":
    input = open("01/input1.txt").readline().strip()

    res = solveIt(input)
    print(f"1 Result is {res}")

    res2 = solveIt2(input)
    print(f"2 Result is {res2}")
