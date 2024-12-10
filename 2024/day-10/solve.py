
data = [list(map(int, list(x))) for x in open("input").read().splitlines()]

DIRECTIONS = [(1,0), (0,1), (-1, 0), (0, -1)]
class Step(object):
    
    def __init__(self, pos, level, trail_map):
        self.pos = pos
        self.level = level
        self.trailmap = trail_map
        self.bound_x = len(trail_map)
        self.bound_y = len(trail_map[0])
        self.paths = self.paths_from_trail_map() 

    def print_path(self):
        print(" "*self.level, "Level ", str(self.level), "at", self.pos)
        for p in self.paths:
            p.print_path()

    def paths_from_trail_map(self):
        paths = []
        x,y = self.pos
        potential = [(x+dx, y+dy) for (dx, dy) in DIRECTIONS] 
        for (px, py) in potential:
            if  px < 0 or px >= self.bound_x or py < 0 or py >= self.bound_y:
                continue
            new_level = self.trailmap[px][py]
            if new_level == self.level + 1:
                paths.append(Step((px, py), new_level, self.trailmap))
        return paths
    
    def score(self):
        if self.level == 9:
            return [self.pos]
        else:
            xxx =  []
            for p in self.paths:
                xx = p.score()
                xxx.extend(xx)
            return set(xxx)

    def score2(self):
        if self.level == 9:
            return 1
        else:
            return sum([p.score2() for p in self.paths])


    def __repr__(self):
        return f"level: {self.level}, {self.pos}"

trail_heads = [Step((x,y), Y, data) for x, X in enumerate(data) for y, Y in enumerate(X) if Y == 0]

sol1 = ([len(h.score()) for h in trail_heads])
print("Solution 1", sum(sol1))

sol2 = sum([h.score2() for h in trail_heads])
print("Solution 2", sol2)
