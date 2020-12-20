import itertools

xmas = [int(i) for i in open("input.txt").read().splitlines()]

illegal = 23278925

start=0
stop=1

while(True):
    window = xmas[start:stop]
    currsum = sum(window)
    print(f"currsum={currsum} / window={window}")
    if(currsum < illegal):
        print("Some more...")
        stop = stop + 1
    elif currsum == illegal:
        print(f"\n\nFound it: {window}")
        print(f"Code: {min(window)+max(window)}")
        break
    else:
        print("Too far!")
        start = start + 1
        stop = stop - 1
