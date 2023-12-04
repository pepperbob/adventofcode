import math
from collections import defaultdict

rawinput = open("04/input").read().split("\n")

input = []
for r in rawinput:
    cards = r.split(":")[1]
    wins, hand = map(str.split, cards.split("|"))
    input.append((wins, hand))

res1 = 0
games_played = defaultdict(lambda: 0)
for g, c in enumerate(input):
    games_played[g] += 1 # play current game
    
    wins, hand = c
    winning = len([h for h in hand if h in wins])
    if winning > 0:
        # calculate fancy :see_no_evil:
        res1 += int(math.pow(2, winning-1))
        # part 2: additional next $winning games
        for additional in range(g+1, g+winning+1):
            games_played[additional] += games_played[g]

print(f"1* Result: {res1}")

stack_size = sum(games_played.values())
print(f"2* Result: {stack_size}")
