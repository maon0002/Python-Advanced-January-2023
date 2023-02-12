from collections import deque

caffeine_mlgrms = [int(x) for x in input().split(", ")]
energy_drinks_seq = deque(int(x) for x in input().split(", "))
MAX_CAFFEINE = 300
INITIAL_CAFFEINE = 0
stamat_caffeine = 0

while caffeine_mlgrms and energy_drinks_seq:
    curr_caffeine = caffeine_mlgrms.pop()
    curr_drink = energy_drinks_seq.popleft()
    curr_calc = curr_caffeine * curr_drink
    check = (MAX_CAFFEINE - stamat_caffeine) - curr_calc
    if check >= 0:
        stamat_caffeine += curr_calc
    else:
        energy_drinks_seq.append(curr_drink)
        if stamat_caffeine - 30 < 0:
            stamat_caffeine = 0
        else:
            stamat_caffeine -= 30

if energy_drinks_seq:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks_seq])}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")