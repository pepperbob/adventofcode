
raw = open("input").read().splitlines()

# split raw input in rules and pages
rules = [x.split("|") for x in raw[:raw.index("")]]
pages = [x.split(",") for x in raw[raw.index("")+1:]]

# some helpful functions
def pages_before(p, rr):
    return set([x[0] for x in rr if x[1]==p])

def get_offending_pages(pp, rr):
    offending = []
    for i, p in enumerate(pp):
        # find overlap of remainding pages with pages before the current page
        if (set(pp[i:]) & pages_before(p, rr)):
            offending.append(p)
    return offending

# extract the middle element of each row in a 2d array
def get_middle_column(arr):
    return [p[int((len(p)-1)/2)] for p in arr]

# collcet results
pages_in_order = []
pages_not_in_order = []
for p in pages:
    offending = get_offending_pages(p, rules)
    if not offending:
        pages_in_order.append(p)
    else:
        # collect pages and offenders
        pages_not_in_order.append((p, offending))

# sum up middle item for solution 1
res = sum(map(lambda x: int(x), get_middle_column(pages_in_order)))
print(f"Solution 1: {res}")

# -- part 2 --
## collect reordered pages
pages_reordered = []
for p, offender in pages_not_in_order:
    # remove offending pages
    cleared = [x for x in p if x not in offender]

    for o in offender:
        # for every offender, lookup the expected index
        expect_at_index = max([cleared.index(x) for x in pages_before(o, rules) if x in cleared])+1
        # insert offending page at the expected index
        cleared.insert(expect_at_index, o)

    pages_reordered.append(cleared)

# sum up middle item for solution 2
res2 = sum(map(lambda x: int(x), get_middle_column(pages_reordered)))
print("Solution 2:", res2)
