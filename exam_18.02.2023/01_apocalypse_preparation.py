from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = list(int(x) for x in input().split())
items_dict = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}
MEDKIT = 100
created_items = {}

while textiles and medicaments:
    first_textile = textiles.popleft()
    last_med = medicaments.pop()
    curr_sum = first_textile + last_med
    #  If their sum is equal to any of the items in the table below create that item and remove both values.
    if curr_sum in items_dict.keys():
        created_item = items_dict[curr_sum]
        if created_item not in created_items.keys():
            created_items[created_item] = 0
        created_items[created_item] += 1

    elif curr_sum > MEDKIT:
        created_item = items_dict[MEDKIT]
        if created_item not in created_items.keys():
            created_items[created_item] = 0
        created_items[created_item] += 1
        diff = curr_sum - MEDKIT
        temp_med = medicaments.pop()
        temp_med += diff
        medicaments.append(temp_med)
    else:
        temp_increase = 10
        last_med += temp_increase
        medicaments.append(last_med)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

final_items_list = []
if created_items:
    sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
    for pair in sorted_items:
        str_to_append = f"{pair[0]} - {pair[1]}"
        final_items_list.append(str_to_append)

print("\n".join(x for x in final_items_list))

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments[::-1])}")

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")






# from collections import deque
#
# textiles = deque(int(x) for x in input().split())
# medicaments = list(int(x) for x in input().split())
# MEDKIT = 100
# healing_items_dict = {
#     30: ["Patch", 0],
#     40: ["Bandage", 0],
#     100: ["MedKit", 0],
#     200: ["TEST", 0],
# }
#
# while textiles and medicaments:
#     first_textile = textiles.popleft()
#     last_med = medicaments.pop()
#     curr_sum = first_textile + last_med
#
#     if curr_sum in healing_items_dict.keys():
#         healing_items_dict[curr_sum][1] += 1
#
#     elif curr_sum > MEDKIT:
#         healing_items_dict[MEDKIT][1] += 1
#         diff = curr_sum - MEDKIT
#         temp_pop = medicaments.pop()
#         value_to_add = diff + temp_pop
#         medicaments.append(value_to_add)
#     else:
#         last_med += 10
#         medicaments.append(last_med)
#
# if not textiles and not medicaments:
#     print("Textiles and medicaments are both empty.")
# if not textiles and medicaments:
#     print("Textiles are empty.")
# if not medicaments and textiles:
#     print("Medicaments are empty.")
#
# textiles_copy, medicaments_copy = textiles.copy(), medicaments.copy()
# sorted_dict = sorted(healing_items_dict.items(), key=lambda x: (-x[1][1], x[1][0]))
# # print(sorted_dict) # [(100, ['MedKit', 2]), (40, ['Bandage', 1]), (30, ['Patch', 1])]
# final_list = []
# for x in sorted_dict:
#     name = x[1][0]
#     qty = x[1][1]
#     # print(name, qty)
#     if qty > 0:
#         line_to_append = f"{name} - {qty}"
#         final_list.append(line_to_append)
#
# print("\n".join(x for x in final_list))
#
# if medicaments:
#     print(f"Medicaments left: {', '.join(str(x) for x in sorted(medicaments, key=lambda x: -x))}")
# if textiles:
#     print(f"Textiles left: {', '.join(str(x) for x in sorted(textiles, key=lambda x: -x))}")
