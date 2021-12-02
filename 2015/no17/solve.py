
total = 150
pieces = sorted([43, 3, 4, 10, 21, 44, 4, 6, 47, 41, 34, 17, 17, 44, 36, 31, 46, 9, 27, 38])

#total = 25
#pieces = [20, 15, 10, 5, 5]

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        return (len(partial), 1)
    elif s >= target:
        return None

    tot = None
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        curr = subset_sum(remaining, target, partial + [n])
        
        if curr is None:
            continue

        if tot is None or curr[0]<tot[0]:
            tot = curr
        elif curr[0] == tot[0]:
            tot = (tot[0], tot[1]+curr[1])

    return tot 

print(subset_sum(pieces, total))