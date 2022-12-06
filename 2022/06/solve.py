class CommunicationMarkerFrame:
    def __init__(self, size = 4) -> None:
        self.buffer = []
        self.index = 0
        self.size = size

    def process(self, x):
        self.buffer.append(x)
        self.index += 1
        
        if (len(self.buffer) > self.size):
            self.buffer.pop(0)
    
    def readMarker(self):
        return self.index if len(self.buffer) == self.size and len(set(self.buffer)) == self.size else None 


input = open("input", "r").read()

# Part 1
startMarker = CommunicationMarkerFrame(size=4)
for i in input:
    startMarker.process(i)
    if startMarker.readMarker() is not None:
        print(f"Marker found at Pos. {startMarker.readMarker()}")
        break


# Part 2
messageMarker = CommunicationMarkerFrame(size=14)
for i in input:
    messageMarker.process(i)
    if messageMarker.readMarker() is not None:
        print(f"Message Marker found at Pos. {messageMarker.readMarker()}")
        break
