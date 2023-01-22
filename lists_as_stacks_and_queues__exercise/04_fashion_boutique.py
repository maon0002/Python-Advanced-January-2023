
stack_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
current_rack = rack_capacity
racks = 1
while stack_of_clothes:
    current_stack = stack_of_clothes.pop()

    if current_stack <= current_rack:
        current_rack -= current_stack

    else:
        current_rack = rack_capacity
        current_rack -= current_stack
        racks += 1
print(racks)












# clothes = [int(n) for n in input().split()]
# rack_space = int(input())
#
# racks_count = 1
# current_rack_space = rack_space
#
# while clothes:
#     cloth = clothes.pop()
#
#     if current_rack_space - cloth >= 0:
#         current_rack_space -= cloth
#     else:
#         racks_count += 1
#         current_rack_space = rack_space - cloth
#
# print(racks_count)
