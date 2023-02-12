def forecast(*args):
    args_list = [[args[i][0], args[i][1]] for i in range(len(args))]
    # print(args_list)

    lst = [f"{x[0]} - {x[1]}" for x in args]
    # print(lst)

    sort_priority = {
        "Sunny": 1,
        "Cloudy": 2,
        "Rainy": 3,}

    final_dict = {}
    for pair in args:
        loc = pair[0]
        forecast = pair[1]
        priority = 0
        if forecast in sort_priority.keys():
            priority = sort_priority[forecast]
        final_dict[loc] = [forecast, priority]
    # print(final_dict)
    sorted_final_dict = sorted(final_dict.items(), key= lambda x: [x[1][1], x[0]])
    # print(sorted_final_dict)

    output = [f"{x[0]} - {x[1][0]}" for x in sorted_final_dict]
    return "\n".join(output)

#
# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))


# def forecast(*args):
#     args_list = [[args[i][0], args[i][1]] for i in range(len(args))]
#     print(args_list)
#
#     def sort_by_forecast(lst):
#         # (('Sofia', 'Sunny'), ('London', 'Cloudy'), ('New York', 'Sunny'))
#         sorted_list = []
#         sort_priority = {
#             "Sunny": 1,
#             "Cloudy": 2,
#             "Rainy": 3,
#         }
#
#         return sorted_list
#
#     sort_by_forecast(args_list)
#     # print(list(args), "nosort")
#     # print(list(args).sort(reverse=True), "sorted")
#     # list.sort(reverse=True | False, key=myFunc)
#     lst = [f"{x[0]} - {x[1]}" for x in args]
#     print(lst)
#     for pair in args:
#         loc = pair[0]
#         forecast = pair[1]