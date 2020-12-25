

def loop_it(loop_size, subj):
    public_key = 1
    for l in range(loop_size):
        public_key = (public_key * subj) % 20201227
    
    return public_key

def reverse_loop_size(public_key):
    loop_size = 0
    calculated_public_key = 1
    while public_key != calculated_public_key:
        loop_size += 1
        calculated_public_key = (calculated_public_key * 7) % 20201227
        if loop_size % 10 == 0:
            print(f"Loop {loop_size} = {calculated_public_key}")
        
    return loop_size


#Test Input:
#pk_card = 5764801
#pk_door = 17807724

pk_card = 6930903
pk_door = 19716708

#lz_card = reverse_loop_size(pk_card)

lz_door = reverse_loop_size(pk_door)
print(lz_door)
print(loop_it(lz_door, pk_card))

# print(lz_door)
# print(loop_it(lz_card, pk_door))