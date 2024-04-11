
input = [int(x) for x in open("input", "r").read().splitlines()]
diff = sum(input)

print(f"Solutation #1 = {diff}")


# first scan of frequencies
rsum = 0
scans = []
for f in input:
    rsum += f
    scans.append(rsum)

max_scan = max(scans) # for optimization

# look for a number that is in first scan of frequencies
n = 1
found = False
while not found:
    for f in scans:
        f_after_n_iterations = f + n * diff
        
        if f_after_n_iterations > max_scan:
            # no need to look further
            continue
        elif f_after_n_iterations in scans:
            print(f"Solutation #2 = {f_after_n_iterations}")

            found = True
            break

    n += 1
