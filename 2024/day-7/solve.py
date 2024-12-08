import math

data = [x.split(": ") for x in open("input").read().splitlines()]

def concat(a, b):
    # this works because b < 100
    return a*100+b

class Item(object):
    def __init__(self, expected, start = 0):
        self.expected = expected
        self.current = start
        self.child = []

    def append(self, no):
        if self.current > self.expected:
            # values can only go up, so shortcut here..
            return

        # root node
        if self.current == 0:
            self.current = no
        elif not self.child:
            self.child.append(Item(self.expected, self.current + no))
            self.child.append(Item(self.expected, self.current * no))
            if RUN_SOLUTION_2:
                self.child.append(Item(self.expected, concat(self.current, no)))
        else:
            for c in self.child:
                c.append(no)

    def number_match_expected(self):
        if not self.child:
            return 1 if self.current == self.expected else 0
        return sum([c.number_match_expected() for c in self.child])

RUN_SOLUTION_2 = True

result = 0
for r in data:
    (expected, items) = r
    current = Item(int(expected))
    for i in items.split(" "):
        current.append(int(i))
    
    result += int(expected) if current.number_match_expected() else 0


print("Solution: ", result)

