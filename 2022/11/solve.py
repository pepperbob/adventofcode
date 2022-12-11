import re 
import math
from functools import reduce

FIND_ALL_NUMBERS = re.compile(r"\d+")
FIND_MONKEY_ID = re.compile(r"monkey (\d+)")

class Monkey:
    
    def __init__(self, name, items, operation, test, ifTrue, ifFalse) -> None:
        self.id = FIND_ALL_NUMBERS.findall(name)[0]
        self.name = f"Monkey {self.id}"
        self.items = [int(x) for x in FIND_ALL_NUMBERS.findall(items)]
        self.operation = re.compile(r"Operation.*: new\s+=(.+)").findall(operation)[0].strip()
        self.test = int(FIND_ALL_NUMBERS.findall(test)[0])
        self.ifTrue = FIND_MONKEY_ID.findall(ifTrue)[0]
        self.ifFalse = FIND_MONKEY_ID.findall(ifFalse)[0]
        self.inspectedItems = 0
        self.divisor = 1
    
    def withWorryLevel(self, wl):
        self.worryLevel = wl

    def setCommonDivisor(self, div):
        self.divisor = div

    def inspectAndThrow(self, monkeys):
        for i in range(len(self.items)):
            self.inspectedItems += 1
            old = self.items.pop(0)
            new = (eval(self.operation.replace("old", f"{old}")) % self.divisor) // self.worryLevel
            if new % self.test == 0:
                monkeys[self.ifTrue].accept(new)
            else:
                monkeys[self.ifFalse].accept(new)

    def accept(self, item):
        self.items.append(item)

    def __repr__(self) -> str:
        return f"{self.name}, {self.items}, {self.operation}, {self.test}, {self.ifTrue}/{self.ifFalse}"

def initMonkeys(notes, worry=3):
    monkeys = dict()
    for note in notes:
        m = Monkey(*note)
        m.withWorryLevel(worry)
        monkeys[m.id] = m

    # update all monkeys with a common modulo divisor, to just keep remainders and 
    # handle very large numbers of part 2
    monkeys_divisor = reduce(lambda x, y: x * y, [x.test for x in monkeys.values()])
    for m in monkeys.values():
        m.setCommonDivisor(monkeys_divisor)

    return monkeys

input = [s.split("\n") for s in open("input", "r").read().split("\n\n")]


# Part 1
monkeys = initMonkeys(input)
for round in range(20):
    for monkey in monkeys.values():
        monkey.inspectAndThrow(monkeys)

sumMostActive = sorted([x.inspectedItems for x in monkeys.values()])[-2:]
print(f"Part 1: Mult. of 2 most active: {math.prod(sumMostActive)}")


# Part 2
monkeys = initMonkeys(input, 1)

for round in range(10000):
    for monkey in monkeys.values():
        monkey.inspectAndThrow(monkeys)

sumMostActive = sorted([x.inspectedItems for x in monkeys.values()])[-2:]
print(f"Part 2: Mult. of 2 most active: {math.prod(sumMostActive)}")
