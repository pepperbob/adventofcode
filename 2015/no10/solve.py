
def look_and_say(tosay):
    prev = tosay[0]
    count = 1
    out = ""
    for n in tosay[1:]:
        if (n == prev):
            count += 1
        else:
            out += f"{count}{prev}"
            count = 1
        
        prev = n

    out += f"{count}{prev}"

    return out

input = "1113122113"
for i in range(50):
    input = look_and_say(input)

print(len(input))