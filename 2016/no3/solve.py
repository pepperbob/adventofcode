
def count_possibles(triangles):
    possibles = 0
    for i in triangles:
        if i[0] + i[1] > i[2] and i[1] + i[2] > i[0] and i[2] + i[0] > i[1]:
            possibles = possibles + 1

    return possibles


input = open("input.txt").read().splitlines()

all_triangles = []
triangle = ()
for i in input:
    for ii in i.strip().split(" "):
        if ii != "":
            triangle = triangle + (int(ii),)
    all_triangles.append(triangle)
    triangle = ()

print(f"1: There are {count_possibles(all_triangles)} possible.")

edged1 = ()
edged2 = ()
edged3 = ()
all_other = []
for t in all_triangles:
    edged1 += (t[0],)
    edged2 += (t[1],)
    edged3 += (t[2],)
    if len(edged1) == 3:
        all_other.append(edged1)
        all_other.append(edged2)
        all_other.append(edged3)
        edged1 = ()
        edged2 = ()
        edged3 = ()

print(f"2: There are {count_possibles(all_other)} possible.")