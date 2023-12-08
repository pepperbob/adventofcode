
input = open("05/input-test2").read().split("\n")
# append empty space
if len(input[-1]) > 0:
    input.append("")

# prepare input nicely
seeds = list(map(int, input[0].split(" ")[1:]))

curr = None
ranges = []
almanac = dict()
for i in input[2:]:
    if i.endswith("map:"):
        curr = i.split(" ")[0]
    elif len(i)==0:
        almanac[curr] = ranges
        ranges = []
        curr = None
    else:
        ranges.append(list(map(int, i.split(" "))))

# part 1
def map_source_to_dest(source, ranges):
    for r in ranges:
        rdest, rsrc, rspan = r
        if rsrc <= source < rsrc+rspan:
            return rdest+source-rsrc
    return source

def lookup_almanac(seed, al):
    source = seed
    for a in al.keys():
        source = map_source_to_dest(source, al[a])
    return source

res1 = min([lookup_almanac(s, almanac) for s  in seeds])
print(f"1* Result: {res1}")

# part 2: same with ranges?
# does not work though
def map_sourcer_to_destr(sourcer, ranges):
    for r in ranges:
        in_from, in_to = sourcer
        rdest, rsrc, rspan = r
        rsrc_from, rsrc_to = rsrc, rsrc+rspan-1

        if in_from <= rsrc_to and in_to >= rsrc_from:
            # it overlapps

            fit_range_from = max(in_from, rsrc_from)
            fit_range_to = min(in_to, rsrc_to)

            # emit lower end range
            if in_from < rsrc_from:
                #yield (in_from, rsrc_from-1)
                pass

            # emit higher end range
            if  rsrc_to < in_to:
                # yield (rsrc_to+1, in_to)
                pass

            add_lower = fit_range_from - rsrc_from
            subst_upper = rsrc_to - fit_range_to
            
            yield (rdest+add_lower, rdest+rspan-1-subst_upper)   
        else:
            yield sourcer

def lookup_almanacr(seedr, al):
    thelist = [seedr]
    for a in al.keys():
        xxx = []
        for x in thelist:
            xxx += list(map_sourcer_to_destr(x, al[a]))
        thelist = xxx
    return thelist

seed_pairs = [(seeds[i], seeds[i] + seeds[i+1] - 1) for i in range(0, len(seeds), 2)]

res2 = [set(lookup_almanacr(s, almanac)) for s in seed_pairs]

print(res2)
mmm = min([x[0] for y in res2 for x in y])
# res2 = [set(lookup_almanacr((s,s), almanac)) for s in seeds]

print(mmm)