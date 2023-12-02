# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
import re

regex = re.compile("Valve\s(..).+rate=(\d+).+valves?(.+)")

class Pipe:
    
    def __init__(self, name, pressure, connectedTo) -> None:
        self.name = name
        self.pressure = pressure
        self.connectedTo = connectedTo
        self.pressureFlow = 0
        self.opened = False

    def flowRate(self):
        return self.pressureFlow

    def open(self):
        self.opened = True
        self.pressureFlow = self.pressure
        pass

    def shallOpen(self):
        return self.pressure > 0 and self.isClosed()

    def isClosed(self):
        return not self.opened

    def __repr__(self) -> str:
        return f"Valve {self.name} is open {self.opened} releasing {self.pressureFlow} ({self.connectedTo})"

ratesAndPipes = [regex.findall(x) for x in open("input-test", "r").read().strip().split("\n")]
ratesAndPipesMap = dict()
for i in [y for x in ratesAndPipes for y in x]:
    current, pressure, pipes = i
    ratesAndPipesMap[current] = Pipe(name=current, pressure=int(pressure), connectedTo=pipes.replace(" ", "").split(","))


# start here
currentPipe = ratesAndPipesMap["AA"]
visited = []

minutes = 0
pressureSum = 0
while minutes < 31:
    minutes += 1

    visited.append(currentPipe.name)
    print(visited)
    
    # collect pressureFlow of all pipes
    pressureSum += sum([p.flowRate() for p in ratesAndPipesMap.values()])

    # collect next pipes
    nextPipes = [ratesAndPipesMap[p] for p in currentPipe.connectedTo]
    
    # iterate next pipes
    for p in nextPipes:
        if p.isClosed() and p.pressure <= currentPipe.pressure:
            # look at next p
            print("look next...")
            currentPipe.open()
            break

        if p.isClosed() and p.pressure > currentPipe.pressure:
            print("move there")
            currentPipe = p
            break
        
        if currentPipe.shallOpen():
            currentPipe.open()
            break

        if p.isClosed() and p.name not in visited:
            currentPipe = p
            break

        currentPipe = ratesAndPipesMap["AA"]

print(pressureSum)