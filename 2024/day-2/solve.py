
input = open("input").read().splitlines()

input = [list(map(lambda x: int(x), i.split(" "))) for i in input]

def isSafe(rep):
    orientation = None
    for level, (x, y) in enumerate(zip(rep, rep[1:])):    
        dif = y - x 
        updown = "decrease" if dif < 0 else "increase"

        if dif == 0:
            return level

        if orientation == None:
            orientation = updown
        elif orientation != updown:
            return level

        if abs(dif) < 1 or abs(dif) > 3:
            return level

    return None

if __name__ == "__main__":

    safe = 0
    for report in input:
        res = isSafe(report)
        if res is None:
            safe += 1
        else:
            print(f"Report {report} = {res}")

    # safe = len(input) - unsafe
    print(f"Solution 1: {safe}")
