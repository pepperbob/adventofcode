data = list(map(int, open("input").read().strip().split(" ")))

cachemap = {}
def cache(fn, arg1, arg2):
    if (arg1, arg2) not in cachemap:
        cachemap[(arg1, arg2)] = fn(arg1, arg2)

    return cachemap[(arg1, arg2)]

def process_recursive(no, count):
    """ items are actually irrelevant, what counts is the item count
    so recursively calclate for every item and sum up the number of elements
    """
    if count == 0:
        # we're done here
        return 1
    if no == 0:
        return cache(process_recursive, 1, count-1)
    elif len(str(no))%2==0:
        stno = str(no)
        lstr = len(stno)//2
        return cache(process_recursive,int(stno[0:lstr]), count-1) + process_recursive(int(stno[lstr:]), count-1)
    else:
        return cache(process_recursive,no*2024, count-1)

sol1 = [cache(process_recursive, n, 25) for n in data]
print("Solution 1", sum(sol1))

sol2 = [cache(process_recursive, n, 75) for n in data]
print("Solution 2", sum(sol2))
