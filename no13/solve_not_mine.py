# read in aoc input and setup to vars from instructions
time = int(open("input.txt").read().strip().split()[0])
buses = open("input.txt").read().strip().split()[1].split(',')
departures = {}

# part 1
for bus in buses:
    if bus != 'x':
        bus_id = int(bus)
        # calculate closest departure to your time for each bus
        departing = (bus_id * (time // bus_id)) + bus_id
        departures[departing] = bus_id

# calculate the wait for the earliest (min) departing bus
wait = min(departures) - time
print(f'Part 1: {wait * departures[min(departures)]}')

# part 2
t, step = 0, 1

# grab all bus id's and time offset
p2 = [(int(i), j) for j, i in enumerate(buses) if i != 'x']

# iterate through buses
for bus_id, mins in p2:
    # check to see if bus is departing at current time
    while (t + mins) % bus_id != 0:
        t += step
    # increase step multiple to find next min for next bus
    step *= bus_id

print(f'Part 2: {t}')
