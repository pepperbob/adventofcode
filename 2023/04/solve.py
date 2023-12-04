import math

rawinput = open("04/input").read().split("\n")

input = []
for r in rawinput:
    cards = r.split(":")[1]
    wins, hand = cards.split("|")
    wins = [x for x in wins.split(" ") if len(x) > 0]
    hand = [x for x in hand.split(" ") if len(x) > 0]
    input.append((wins, hand))


res1 =  0
game_wins = dict()

for g, c in enumerate(input):
    game_wins[g] = []

    wins, hand = c
    hand_win = [h for h in hand if h in wins]
    winning_cards = len(hand_win)
    if winning_cards > 0:
        # calculate fancy :see_no_evil:
        res1 += int(math.pow(2, len(hand_win)-1))
        # memorize stacks copied
        game_wins[g] = [g+x for x in range(1, winning_cards+1)]  

print(f"1* Result: {res1}")

# recursion, crazy slow
def get_stack_size(game, win_map):
    local_stack = 1
    for x in win_map[game]:
        local_stack += get_stack_size(x, win_map)
    return local_stack

# add stack size
stack_size = 0
for g in game_wins.keys():
    stack_size += get_stack_size(g, game_wins)

print(f"2* Result: {stack_size}")
