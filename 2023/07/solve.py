
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

    print(hand)
    # for part 2 modify whatever is fingerprinted for the "J"
    sort_for_joker = sorted([(y, hand.count(y), 12 - strengths.index(y)) for y in hand_set], key=lambda x: (x[1], x[2]))
    # print(f"  joker sort: {sort_for_joker}")
    j_is, a, b = sort_for_joker[-1]
    if "J" in hand:
        print(f"  Joker {j_is}")
    jokered_hand = hand.replace("J", j_is) # replace J with card of most occurence, maybe J
    jokered_hand_set = set(jokered_hand)

    fingerprint = "".join(list(sorted([str(hand.count(y)) for y in hand_set], reverse=True)))
    jokered_fingerprint = "".join(list(sorted([str(jokered_hand.count(y)) for y in jokered_hand_set], reverse=True)))
    # print(f"Std  : {hand} -> {fingerprint}")
    if jokered_fingerprint != fingerprint:
        print(f"  impr.: {hand} -> {jokered_fingerprint}")
    inter.append((hand, hand_weights, bid, games[jokered_fingerprint]))

ranked = sorted(inter, key = lambda x: (x[3], x[1]))

res = sum([x[2]* (i+1) for i, x in enumerate(ranked)])

print(f"1* Result: {res} ")