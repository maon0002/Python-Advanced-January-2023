def words_sorting(*args):
    words_dict = {x: None for x in args}

    for key in words_dict.keys():
        total = []
        for char in key:
            total.append(ord(char))
        words_dict[key] = sum(total)

    sum_of_all_dict_values = sum([x for x in words_dict.values()])
    if sum_of_all_dict_values % 2 == 0:
        final_list = sorted(words_dict.items(), key=lambda x: x[0])
    else:
        final_list = sorted(words_dict.items(), key=lambda x: -x[1])
    result = []
    for word, value in final_list:
        result.append(f"{word} - {value}")

    return "\n".join(result)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))

#
# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))
#
#
# print(
#     words_sorting(
#         'cacophony',
#         'accolade'
#   ))
