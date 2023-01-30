from collections import deque

string = deque(_ for _ in input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}

collected_colors = list()

colors_dict = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'},
}

while string:
    current_color = ""

    if len(string) == 1:
        last_substring = string.pop()
        if last_substring in all_colors:
            collected_colors.append(last_substring)
            break
    elif len(string) > 1:
        start = string.popleft()
        end = string.pop()
        middle = len(string) // 2
        if (start + end) in all_colors or (end + start) in all_colors:
            if (start + end) in all_colors:
                collected_colors.append(start + end)
            else:
                collected_colors.append(end + start)
        else:
            add_in_the_middle = start[:-1] + end[:-1]
            string.insert(middle, add_in_the_middle)

# for sec_color in collected_colors:
#     if sec_color in colors_dict.keys():
#         for needed_color in colors_dict[sec_color]:
#             if needed_color not in collected_colors:
#                 collected_colors.remove(sec_color)

for sec_color in set(colors_dict.keys()).intersection(collected_colors):
    if not colors_dict[sec_color].issubset(collected_colors):
        collected_colors.remove(sec_color)


print(collected_colors)


# for color in set(req_colors.keys()).intersection(result):
#     if not req_colors[color].issubset(result):
#         result.remove(color)












# from collections import deque
#
# words = deque(input().split())
#
# colors = {"red", "yellow", "blue", "orange", "purple", "green"}
# req_colors = {
#     "orange": {"red", "yellow"},
#     "purple": {"red", "blue"},
#     "green": {"yellow", "blue"},
# }
#
# result = []
#
# while words:
#     first_word = words.popleft()
#     second_word = words.pop() if words else ''
#
#     for color in (first_word + second_word, second_word + first_word):
#         if color in colors:
#             result.append(color)
#             break
#     else:
#         for el in (first_word[:-1], second_word[:-1]):
#             if el:
#                 words.insert(len(words) // 2, el)
#
# for color in set(req_colors.keys()).intersection(result):
#     if not req_colors[color].issubset(result):
#         result.remove(color)
#
#
# print(result)
