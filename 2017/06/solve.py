
input = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
memory = [int(x) for x in input.split("\t") if x != ""]
distribute_over = len(memory)

seen_configs = []
cycle = 0
loop_size = 0
while True:
    current_config = " ".join([str(x) for x in memory])
    if current_config in seen_configs:
        first_seen = seen_configs.index(current_config)
        loop_size = cycle - first_seen
        break

    seen_configs.append(current_config)
    
    cycle += 1
    distribute_memory = max(memory)
    current_bank = memory.index(distribute_memory)
    memory[current_bank] = 0
    while distribute_memory > 0:
        current_bank = (current_bank + 1) % distribute_over
        memory[current_bank] += 1
        distribute_memory -= 1

print(f"1* Result: {cycle}")
print(f"2* Result: {loop_size}")
