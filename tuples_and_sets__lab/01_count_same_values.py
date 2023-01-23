nums = tuple([float(x) for x in input().split()])

nums_dict = {}

for i in range(len(nums)):
    num = nums[i]
    if num not in nums_dict:
        nums_dict[num] = 0
    nums_dict[num] += 1

for k,v in nums_dict.items():
    print(f"{k} - {v} times")

# (-2.5, 4.0, 3.0, -2.5, -5.5, 4.0, 3.0, 3.0, -2.5, 3.0)
# {-2.5: 3, 4.0: 2, 3.0: 4, -5.5: 1}












# lst = ['', 0, False, None, ' ', []]
# for x in lst:
#     print(x, hash(x))

#
# values = tuple(map(float, input().split(' ')))
# values_counter = {}
#
# for value in values:
#     if value not in values_counter:
#         values_counter[value] = 0
#     values_counter[value] += 1
#
# for k, v in values_counter.items():
#     print(f'{k} - {v} times')


