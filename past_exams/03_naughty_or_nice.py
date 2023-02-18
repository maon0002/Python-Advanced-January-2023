def naughty_or_nice_list(*args, **kwargs):
    CONDITIONS_LIST = ['Nice', 'Naughty', 'Not found']
    santa_list = {
        'Nice': [],
        'Naughty': [],
        'Not found': [],
    }
    args_list = args[0]  # [(3, 'Amy'), (1, 'Tom'), (7, 'George'), (3, 'Katy'), (2, 'Katy')]
    # unique = [print(x) for x in args_list if args_list[0].count(int(x[0])) == 0]
    # unique = [x for x in args_list if args_list[0].count(int(x[0])) == 0]
    # non_unique = [x for x in args_list if args_list[0].count(int(x[0])) == 1]
    distinct_digits = {}
    for i in range(len(args_list)):
        curr_digit = args_list[i][0]
        curr_name_ = args_list[i][1]
        if curr_digit not in distinct_digits.keys():
            distinct_digits[curr_digit] = []
        distinct_digits[curr_digit].append(curr_name_)

    param = {}  # {3: 'Nice', 1: 'Naughty'}
    for command in args[1:]:
        command_split = command.split("-")
        digit = int(command_split[0])
        nice_or_naughty = command_split[1]
        param[digit] = nice_or_naughty

    for pair in args_list:
        digit_ = pair[0]
        name = pair[1]
        if len(distinct_digits[digit_]) < 2:
            if digit_ in param.keys():
                move_to = param[digit_]
                santa_list[move_to].append(name)
            else:
                santa_list['Not found'].append(name)

    distinct_names = {}
    for i in range(len(args_list)):
        curr_name = args_list[i][1]
        if curr_name not in distinct_names.keys():
            distinct_names[curr_name] = 0
        distinct_names[curr_name] += 1

    print(distinct_names)

    for x in kwargs.items():
        name_kwargs = x[0]
        nice_or_naughty_kwargs = x[1]
        if distinct_names[name_kwargs] == 1:
            santa_list[nice_or_naughty_kwargs].append(name_kwargs)

    return santa_list


# print(naughty_or_nice_list(
#     [
#         (3, "Amy"),
#         (1, "Tom"),
#         (7, "George"),
#         (3, "Katy"),
#         # (2, "Katy"),
#     ],
#     "3-Nice",
#     "1-Naughty",
#     Amy="Nice",
#     Katy="Naughty",
# ))

#
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
# ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))


# def naughty_or_nice_list(*args, **kwargs):
#     CONDITIONS_LIST = ['Nice', 'Naughty', 'Not found']
#     santa_list = {
#         'Nice': [],
#         'Naughty': [],
#         'Not found': [],
#     }
#     args_list = args[0]
#
#     # duplicates = any([True for x in args_list if args_list.count(x) > 1])
#     exact_duplicate_rec = set(x for x in args_list[0] if args_list.count(x[0]) > 1)
#     print(exact_duplicate_rec)
#
#     print(args_list)
#
#     for i in range(1, len(args)):
#         pair = args[i]
#         num, move_to_list = pair.split("-")
#         counter_n = 0
#         for n in args_list[0]:
#             if n == int(num):
#                 counter_n += 1
#         if counter_n == 1:
#             for _ in range(len(args_list)):
#                 curr_tuple = args_list[_]
#                 curr_num = curr_tuple[0]
#                 curr_name = curr_tuple[1]
#
#         if int(num) in exact_duplicate_rec:
#             continue
#         else:
#
#     for kid, status in kwargs.items():
#         print(kid, status)
#
#     # for _ in range(len(args)):
#     #     element = args[_]
#     #     temp_lst = []
#     #     if type(element) == list:
#     #         for el in element:
#     #             duplicates = any([True for x in element if element.count(x) > 1])
#     #             exact_duplicate_rec = tuple(x for x in element if element.count(x) > 1)
#     #             print("dupl:", duplicates)
#     #             print("exact_dupl:", exact_duplicate_rec)
#     #             counting_number = el[0]
#     #             name = el[1]
#     #             temp_lst.append(el)
#     #             print(temp_lst, "temp")
#     #
#     #
#     #             # print(el, counting_number, name)
#     #     elif type(element) == str:
#     #         num_str, condition = element.split("-")
#     #         if condition == "Nice":
#     #             nice = int(num_str)
#     #         elif condition == "Naughty":
#     #             naughty = int(num_str)
#     #
#     # for pair in args:
#     #     count = pair[0]
#     #     name = pair[1]
