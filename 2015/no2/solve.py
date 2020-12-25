

measures = [tuple(i.strip().split("x")) for i in open("input.txt").read().strip().split("\n")]
measures = [(int(t[0]), int(t[1]), int(t[2])) for t in measures]

# area

total_area = 0
for m in measures:
    ms = (m[0]*m[1], m[1]*m[2], m[0]*m[2])
    total_area += sum(ms)*2 + min(ms)

print(f"Total Area: {total_area}")

# ribbon
total_feet = 0
for m in measures:
    l,w,h = m
    total_feet += l*w*h + 2*sum(sorted(m)[:2])

print(f"Total Ribbon: {total_feet}")