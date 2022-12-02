
# A/X = Rock
# B/Y = Paper
# C/Z = Scissors

# Solve with lookup tables

# score for my choices
rps_scores = {
 "X": 1,
 "Y": 2,
 "Z": 3,
}

# possible games and outcomes (0-loose, 3-draw, 6-win)
rps_game = {
  "AX": 3,
  "AY": 6,
  "AZ": 0,
  "BX": 0,
  "BY": 3,
  "BZ": 6,
  "CX": 6,
  "CY": 0,
  "CZ": 3
}


input = [r.split() for r in open("input", "r").read().split("\n") if r != ""]

# Part 1
total = 0
for i in input:
    res = "".join(i)
    # lookup score of my choice
    base_score = rps_scores[i[1]]
    # lookup score of game
    shape_score = rps_game[res]
    # add everything
    total += shape_score+base_score

print(f"Part 1: Total = {total}")

# Part 2

# A = Rock
# B = Paper
# C = Scissors
# X = Loose / Rock
# Y = Draw  / Paper
# Z = Win   / Scissors

# oh god, annoyingly made another mapping table to select for outcome
# use above reference
rps_win_loose = {
  "AX": "Z",
  "AY": "X",
  "AZ": "Y",
  "BX": "X",
  "BY": "Y",
  "BZ": "Z",
  "CX": "Y",
  "CY": "Z",
  "CZ": "X"
}

total_pt2 = 0
for i in input:
    res = "".join(i)

    # lookup my choice
    my_choice = rps_win_loose[res]
    
    # map to corresponding "part 1 coding"
    res = res[0] + my_choice

    base_score = rps_scores[my_choice]
    shape_score = rps_game[res]
    total_pt2 += shape_score+base_score

print(f"Part 2: Total = {total_pt2}")