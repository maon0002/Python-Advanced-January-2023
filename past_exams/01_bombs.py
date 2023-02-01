from _collections import deque

first_bomb_effect = deque(int(x) for x in input().split(", "))
last_bomb_casing = [int(x) for x in input().split(", ")]

bombs_dict = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs",
}

bombs_inventory = dict()

while first_bomb_effect and last_bomb_casing:
    first = first_bomb_effect.popleft()
    last = last_bomb_casing.pop()
    if first + last in bombs_dict.keys():
        if bombs_dict[first + last] not in bombs_inventory:
            bombs_inventory[bombs_dict[first + last]] = 0
        bombs_inventory[bombs_dict[first + last]] += 1
    else:
        last_bomb_casing.append(last - 5)
        first_bomb_effect.appendleft(first)

inventory = []

print(bombs_inventory)
