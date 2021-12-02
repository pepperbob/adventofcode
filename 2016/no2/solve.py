
def moves_by(pad):
    min_pos = (0, 0)
    max_pos = (len(pad)-1, len(pad[0])-1)

    onpad = lambda pos: pos[0] >= min_pos[0] and pos[1] >= min_pos[1] and pos[0] <= max_pos[0] and pos[1] <= max_pos[1] and pad[pos[0]][pos[1]] is not None
    onpad_or_keep = lambda old, new: new if onpad(new) else old

    return {
        "U": lambda pos: onpad_or_keep(pos, (pos[0]-1, pos[1])),
        "D": lambda pos: onpad_or_keep(pos,(pos[0]+1, pos[1])),
        "R": lambda pos: onpad_or_keep(pos,(pos[0], pos[1]+1)),
        "L": lambda pos: onpad_or_keep(pos,(pos[0], pos[1]-1))
    }

keypad = [[1,2,3], [4,5,6], [7,8,9]]
keypad_moves = moves_by(keypad)

n = None
awsome_keypad = [[n,n,"1",n,n], [n,"2","3","4",n], ["5","6","7","8","9"], [n,"A","B","C",n],[n,n,"D",n,n]]
awsome_moves = moves_by(awsome_keypad)

def new_arr(pad):
    return [[ 0 for x in range(0,len(pad))] for y in range(0,len(pad[0]))]

def move(new_pos, pad):
    """Creates new Array like Pad and Moves indicator 1 to position"""
    arr = new_arr(pad)
    arr[new_pos[0]][new_pos[1]]=1
    return arr

def current_pos(arr):
    """Finds Position marked 1 on Array"""
    for ix, x in enumerate(arr):
        for iy, y in enumerate(x):
            if y == 1:
                return (ix, iy)
    return (-1, -1)

def move_op(d, arr, moves):
    """Carries out Move Operation d on Array"""
    pos = current_pos(arr)
    new_pos = moves[d](pos)
    return move(new_pos, arr)

def which_key(arr, pad):
    pos = current_pos(arr)
    return pad[pos[0]][pos[1]]


input = open("input.txt").read()

curr = move((1,1), keypad)
key = []
for i in input.splitlines():
    for op in i:
        curr = move_op(op, curr, keypad_moves)
    key.append(which_key(curr, keypad))

print(f"Simple Keypad Key {key}")

curr = move((2,2), awsome_keypad)
key = []
for i in input.splitlines():
    for op in i:
        curr = move_op(op, curr, awsome_moves)
    key.append(which_key(curr, awsome_keypad))

print(f"Awsome Keypad Key {key}")