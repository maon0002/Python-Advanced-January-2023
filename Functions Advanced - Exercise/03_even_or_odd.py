def even_odd(*args):
    command = args[-1]
    nums = [x for x in args if type(x) == int]
    # print(nums)
    if command == "even":
        return [x for x in nums if x % 2 == 0]
    return [x for x in nums if x % 2 != 0]

print(even_odd(1, 2, 3, 4, 5, 6, "even"))














# def even_odd(*args):
#     command = args[-1]














#
#     if command == 'even':
#         return [n for n in args[:-1] if int(n) % 2 == 0]
#     else:
#         return [n for n in args[:-1] if int(n) % 2 == 1]
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))

# def even_odd(*args):
#     command = args[-1]
#     result = []
#
#     for n in args[:-1]:
#         if int(n) % 2 == 0 and command == "even":
#             result.append(n)
#         elif int(n) % 2 == 1 and command == "odd":
#             result.append(n)
#
#     return result