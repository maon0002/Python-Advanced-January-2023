from collections import deque

materials_stack = [int(m) for m in input().split()]
magic_deque = deque(int(n) for n in input().split())

gift_dict = {
    'Gemstone': [range(100, 199 + 1), 0],
    'Porcelain Sculpture': [range(200, 299 + 1), 0],
    'Gold': [range(300, 399 + 1), 0],
    'Diamond Jewellery': [range(400, 499 + 1), 0],
}
crafted = set()
crafted_condition = ({'Gemstone', 'Porcelain Sculpture'}, {'Gold', 'Diamond Jewellery'}) #set subset?
have_pair = False

while materials_stack and magic_deque:
    curr_material = materials_stack.pop()
    curr_magic = magic_deque.popleft()
    gift_try_sum = curr_magic + curr_material

    if gift_try_sum < 100:
        if gift_try_sum % 2 == 0:
            curr_material *= 2
            curr_magic *= 3
            gift_try_sum = curr_magic + curr_material
        else:
            curr_material *= 2
            curr_magic *= 2
            gift_try_sum = curr_magic + curr_material
    elif gift_try_sum > 499:
        curr_material /= 2
        curr_magic /= 2
        gift_try_sum = int(curr_magic + curr_material)

    for items in gift_dict.items():
        gift = items[0]
        points_range = items[1][0]
        if gift_try_sum in points_range:
            gift_dict[gift][1] += 1
            crafted.add(gift)
            break

    if crafted_condition[0].issubset(crafted) or crafted_condition[1].issubset(crafted):
        have_pair = True


print("The wedding presents are made!") if have_pair else print("Aladdin does not have enough wedding presents.")
if materials_stack:
    print(f"Materials left: {', '.join(str(m) for m in materials_stack)}")
if magic_deque:
    print(f"Magic left: {', '.join(str(m) for m in magic_deque)}")

sorted_dict = sorted(gift_dict)
for items in gift_dict.items():
    gift = items[0]
    count = items[1][1]
    if count > 0:
        print(f"{gift}: {count}")