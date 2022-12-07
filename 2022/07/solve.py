import re

class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def getSize(self):
        return self.size

class Directory:
    def __init__(self, name, parent = None) -> None:
        self.name = name
        self.parent = parent
        self.content = []

    def cd(self, dirName):
        return self.parent if dirName == ".." else next(x for x in self.content if x.name == dirName and isinstance(x, Directory))

    def mkdir(self, dirName):
        self.content.append(Directory(name = dirName, parent = self))

    def touch(self, filename, size):
        self.content.append(File(name=filename, size=size))        

    def getSize(self):
        return sum([x.getSize() for x in self.content])

    def listDirs(self):
        theDirs = [(self.name, self.getSize())]
        for d in [x for x in self.content if isinstance(x, Directory)]:
            theDirs.extend(d.listDirs())

        return theDirs


# Parse Input
input = open("input", "r").read().split("\n")

# cmd patterns
cdInDir = r"\$ cd\s(.+)"
dirListing = r"dir\s(.+)"
fileWithSize = r"(\d+)\s(.+)"

root = Directory(name="/")
curr = root

# we have root already:
for l in input[1:]:
    if re.match(cdInDir, l):
        dirName = re.match(cdInDir, l).groups()[0]
        curr = curr.cd(dirName)
    elif re.match(dirListing, l):
        dirName = re.match(dirListing, l).groups()[0]
        curr.mkdir(dirName)
    elif re.match(fileWithSize, l):
        (s, name) = re.match(fileWithSize, l).groups()
        curr.touch(name, int(s))


# Part 1
totalSumPart1 = sum([x[1] for x in root.listDirs() if x[1] <= 100000])

print(f"Part 1 Total: {totalSumPart1}")

# Part 2
totalDiskSpace = 70000000
freeSpaceRequired = 30000000
availableSpace = totalDiskSpace - root.getSize()
spaceToFree = freeSpaceRequired - availableSpace

smallestDirToFreeSpace = min([x[1] for x in root.listDirs() if x[1] >= spaceToFree])

print(f"Part 2 Size: {smallestDirToFreeSpace}")
