

times, distances = open("06/input2").read().splitlines()

times = [int(x.strip()) for x in times.split(":")[1].split(" ") if len(x) > 0]
distances = [int(x.strip()) for x in distances.split(":")[1].split(" ") if len(x)>0]

def winning_config(config):
    time, dist = config
    start = 0
    end = 0
    for t in range(1, time):
        if(t * (time - t) > dist):
            start = t
            break
    
    for t in range(time, 1, -1):
        if(t * (time - t) > dist):
            end = t
            break
    
    return end - start + 1

res1 = 1
for t, d in zip(times, distances):
    res1 *= winning_config((t,d))

print(f"Result 1: {res1}")