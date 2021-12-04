

input = open("input.txt").readlines()

calls = [int(c) for c in input[0].split(",")]

boards = []
curr = None

# read all boards
for b in input[1:]:
    if b.strip() == "":
        curr = []
        boards.append(curr)
        continue

    line = [int(x) for x in b.strip().split(" ") if x != ""]
    curr.append(line)

def did_win(board):
    tmp_board = list(board)

    for i in range(len(tmp_board)):
        add_row = []
        for j in range(len(tmp_board[0])):
            add_row.append(tmp_board[j][i])
        tmp_board.append(add_row)

    # rows:
    for r in tmp_board:
        if all(p == "x" for p in r):
            return True
    
    return False

# register calls
has_winner = False
last = None
last_call = None
winners_so_far = []
for c in calls:
    for no, board in enumerate(boards):
        for i, row in enumerate(board):
            for j, pos in enumerate(row):
                if board[i][j] == c:
                    board[i][j] = "x"
        
        has_winner = did_win(board)
        if has_winner and no not in winners_so_far:
            winners_so_far.append(no)
    
        if len(winners_so_far) == len(boards):
            last_call = c
            last = board
            break
    
    if last is not None:
        break

print("-- Last --")
for r in last:
    print(r)

last_sum = sum([k for x in last for k in x if k != "x"])
print(last_sum * last_call)