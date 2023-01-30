from collections import deque

boxes_with_materials = deque(int(material) for material in input().split())
magic_values = deque(int(material) for material in input().split())

crafts = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}
CONDITION_ONE = {'Doll', 'Wooden train'}
CONDITION_TWO = {'Teddy bear', 'Bicycle'}

crafted = deque()
succeed = False
while boxes_with_materials and magic_values:

    material = boxes_with_materials.pop() if magic_values or not boxes_with_materials else 0
    magic = magic_values.popleft() if magic_values or not boxes_with_materials else 0
    total_magic_lvl = material * magic

    crafted_set = set(crafted)
    if CONDITION_ONE.issubset(crafted_set) or CONDITION_TWO.issubset(crafted_set):
        succeed = True

    if total_magic_lvl in crafts:
        crafted.append(crafts[total_magic_lvl])
        continue

    if material == 0 or magic == 0:
        if material + magic == 0:
            continue
        elif material == 0:
            magic_values.appendleft(magic)
        elif magic == 0:
            boxes_with_materials.append(material)
    elif total_magic_lvl > 0:
        boxes_with_materials.append(material + 15)
    elif total_magic_lvl < 0:
        total_magic_lvl = material + magic
        boxes_with_materials.append(total_magic_lvl)

crafted_dict = dict()
for item in crafted:
    if item not in crafted_dict:
        crafted_dict[item] = 0
    crafted_dict[item] += 1

print("The presents are crafted! Merry Christmas!") if succeed else print("No presents this Christmas!")
if boxes_with_materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(boxes_with_materials))}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

[print(f"{item}: {qty}") for item, qty in sorted(crafted_dict.items())]


#
# from collections import deque
#
# materials = deque(int(x) for x in input().split())
# magic_levels = deque(int(x) for x in input().split())
#
# crafted = []
# presents = {
#     150: "Doll",
#     250: "Wooden train",
#     300: "Teddy bear",
#     400: "Bicycle",
# }
#
# while materials and magic_levels:
#     material = materials.pop() if magic_levels[0] or not materials[0] else 0
#     magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0
#
#     if not magic_level:
#         continue
#
#     product = material * magic_level
#
#     if presents.get(product):
#         crafted.append(presents[product])
#     elif product < 0:
#         materials.append(material + magic_level)
#     elif product > 0:
#         materials.append(material + 15)
#
# if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials:
#     print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")
#
# if magic_levels:
#     print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
#
# [print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
