values_dict = {}
odd_set = set()
even_set = set()
for i in range(int(input())):
    name = input()
    sum_total = 0
    for char in name:
        sum_total += ord(char)
    values_dict[name] = [i + 1, sum_total // (i + 1)]
    sum_total = sum_total // (i + 1)
    odd_set.add(sum_total) if sum_total % 2 != 0 else even_set.add(sum_total)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) < sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=", ")









# odd_set = set()
# even_set = set()
#
# for row in range(1, int(input()) + 1):
#     ascii_sum_of_name = sum(ord(l) for l in input()) // row
#
#     if ascii_sum_of_name % 2 == 0:
#         even_set.add(ascii_sum_of_name)
#     else:
#         odd_set.add(ascii_sum_of_name)
#
# if sum(odd_set) == sum(even_set):
#     print(*odd_set.union(even_set), sep=", ")
# elif sum(odd_set) > sum(even_set):
#     print(*odd_set.difference(even_set), sep=", ")
# else:
#     print(*odd_set.symmetric_difference(even_set), sep=", ")
