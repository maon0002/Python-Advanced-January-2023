records = int(input())
lst = list()
dict_ = {}
idx = 0
lst_result = []
length_comparison = 0

for i in range(records):
    packs = input().split("-")
    for x in packs:
        starts, ends = x.split(",")
        current_range = set(range(int(starts), int(ends) + 1))
        dict_[idx] = current_range
        idx += 1
    if len(dict_[idx - 2].intersection(dict_[idx - 1])) > length_comparison:
        lst_result = list(dict_[idx - 2].intersection(dict_[idx - 1]))
        length_comparison = len(dict_[idx - 2].intersection(dict_[idx - 1]))

print(f"Longest intersection is {lst_result} with length {length_comparison}")






#
# longest_intersection = set()
#
# for _ in range(int(input())):
#     first_data, second_data = [el.split(",") for el in input().split("-")]
#
#     first_range = set(range(int(first_data)[0]), int(first_data[1] + 1))
#     second_range = set(range(int(second_data)[0]), int(second_data[1] + 1))
#
#     intersection = first_range.intersection(second_range)
#
# print(
#     f"Longest intersection is "
#     f"[{', '.join(str(x) for x in longest_intersection)}]"
#     f"with length {len(longest_intersection)}"
# )
