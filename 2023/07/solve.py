
input = [(a, int(b)) for a, b in [x.split(" ") for x in open("07/input").read().splitlines()]]

strengths = "AKQJT98765432" # 12

games = {
"5": 6, # five_of_a_kind
"41": 5, # four_of_a_kind
"32": 4, # full_house
"311": 3, # three
"221": 2, # two_pair
"2111": 1, # one_pair
"11111": 0, # high_card
}

inter = []
for x in input:
    hand, bid = x
    
    hand_weights = [12 - strengths.index(x) for x in hand]
    hand_set = set(hand)
    fingerprint = "".join(list(sorted([str(hand.count(y)) for y in hand_set], reverse=True)))
    print(f"{hand} -> {fingerprint}")
    inter.append((hand, hand_weights, bid, games[fingerprint]))

ranked = sorted(inter, key = lambda x: (x[3], x[1]))

res = sum([x[2]* (i+1) for i, x in enumerate(ranked)])

print(f"1* Result: {res} ")