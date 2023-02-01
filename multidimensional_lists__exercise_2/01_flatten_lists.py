input_line = [[int(n) if n.isdigit() else n for n in x.split(' ')] for x in input().split("|")[::-1]]
result = []
for row in range(len(input_line)):
    for char in input_line[row]:
        if char != "":
            print(int(char), end=' ')



# line = input().split("|")  # прочитаме реда като го разделяме по черта
#
# sub_lists = []  # създаваме списък, в които ще пазим резултата
#
# for sub_string in line[::-1]:  # развъртаме цикъл, който обхожда всеки под-текст в инпута
#     sub_lists.extend(sub_string.split())
#     # удължаваме списъка с резултата със списък от числата от конзолата след като сме махнали всички спейсове
#
# print(*sub_lists)  # ънпакваме списъка
#
# numbers = [string.split() for string in input().split("|")]
# print(*[' '.join(string) for string in numbers[::-1] if string])