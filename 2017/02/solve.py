import itertools

def solveIt(input):
    chk = 0
    for line in input:
        allnums = [int(x) for x in line.split(" ")]
        chk += (max(allnums) - min(allnums))
    return chk

def solveIt2(input):
    chk = 0
    for line in input:
        allnums = [int(x) for x in line.split(" ")]
        even = [int((a/b)) for a,b in itertools.permutations(allnums, 2) if a%b == 0]
        chk += sum(even)
    return chk

if __name__ == "__main__":
    lines = open("02/input1.txt").read().replace("\t", " ").splitlines()

    res = solveIt(lines)
    print(f"1 Result is {res}")

    res2 = solveIt2(lines)
    print(f"2 Result is {res2}")