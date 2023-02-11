from _collections import deque
# 5, 25, 25, 115
# 5, 15, 25, 35
bomb_effect = deque(int(num) for num in input().split(", "))
bomb_casing = [int(num) for num in input().split(", ")]
bombs_dict = {
    40: ['Datura Bombs', 0],
    60: ['Cherry Bombs', 0],
    120: ['Smoke Decoy Bombs', 0],
}
BOMB_POUCH = 3
is_fulfilled = False

while bomb_casing and bomb_effect:

    fulfill_bomb_pouch = all([True if val[1] >= 3 else False for val in bombs_dict.values()])
    if fulfill_bomb_pouch:
        is_fulfilled = True
        break

    current_effect = bomb_effect.popleft()
    current_casing = bomb_casing.pop()
    current_try = current_effect + current_casing
    if current_try in bombs_dict.keys():
        bombs_dict[current_try][1] += 1
    else:
        bomb_casing.append(current_casing - 5)
        bomb_effect.appendleft(current_effect)

ordered_bombs = sorted(bombs_dict.items(), key= lambda x: x[1])
# print(ordered_bombs)
print("Bene! You have successfully filled the bomb pouch!") if is_fulfilled else print("You don't have enough materials to fill the bomb pouch.")
print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}") if bomb_effect else print(f"Bomb Effects: empty")
print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing)}") if bomb_casing else print(f"Bomb Casings: empty")
for ob in ordered_bombs:
    ob = ob[1]
    bomb = str(ob[0])
    bomb_count = str(ob[1])
    print(f"{bomb}: {bomb_count}")

















# from _collections import deque
#
# first_bomb_effect = deque(int(x) for x in input().split(", "))
# last_bomb_casing = [int(x) for x in input().split(", ")]
#
# bombs_dict = {
#     40: "Datura Bombs",
#     60: "Cherry Bombs",
#     120: "Smoke Decoy Bombs",
# }
#
# bombs_inventory = dict()
#
# while first_bomb_effect and last_bomb_casing:
#     first = first_bomb_effect.popleft()
#     last = last_bomb_casing.pop()
#     if first + last in bombs_dict.keys():
#         if bombs_dict[first + last] not in bombs_inventory:
#             bombs_inventory[bombs_dict[first + last]] = 0
#         bombs_inventory[bombs_dict[first + last]] += 1
#     else:
#         last_bomb_casing.append(last - 5)
#         first_bomb_effect.appendleft(first)
#
# inventory = []
#
# print(bombs_inventory)
