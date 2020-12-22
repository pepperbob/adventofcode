#!/usr/bin/env python
import fileinput

#fn="input_test2.txt"
fn="input.txt"

decks = open(fn).read().strip().split("\n\n")

def playgame(p1, p2, game=1):
    p1_hist = []
    p2_hist = []
    print(f"-== Game {game} ==-")
    while len(p1) > 0 and len(p2) > 0:

        if(p1 in p1_hist or p2 in p2_hist):
            return ("Player1", p1)
        
        p1_hist.append(p1.copy())
        p2_hist.append(p2.copy())

        n1 = p1.pop(0)
        n2 = p2.pop(0)

        # check if new game
        if(len(p1) >= n1 and len(p2) >= n2):
            winner = playgame(p1[:n1], p2[:n2], game+1)[0]
        elif(n1 > n2):
            winner = "Player1"
        else:
            winner = "Player2"

        # put cards under stack
        if winner == "Player1":
            p1 += (n1, n2)
        else:
            p2 += (n2, n1)
        
    # return player name?
    winner = ("Player1", p1) if len(p1) > 0 else ("Player2", p2)
    print(f"End of Game {game}, Winner {winner[0]}")
    return  winner


player1 = list(map(lambda s: int(s), decks[0].split("\n")[1:]))
player2 = list(map(lambda s: int(s), decks[1].split("\n")[1:]))

winner = playgame(player1, player2)

score = 0
for a,b in zip(winner[1], reversed(range(len(winner[1])))):
    score += a * (b+1)

print(f"{winner[0]} won with a score of {score}!")
