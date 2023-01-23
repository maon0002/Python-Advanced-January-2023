input_line = tuple(input())
lst = set()
for char in input_line:
    occurrences = input_line.count(char)
    string_ = f"{char}: {occurrences} time/s"
    lst.add(string_)
result_set = {x for x in lst}
result_tuple = sorted(x for x in result_set)
end = [print(x, end='\n') for x in result_tuple]










# occurrences = {}
#
# for letter in input():
#     if letter not in occurrences:
#         occurrences[letter] = 0
#     occurrences[letter] += 1
#
# for letter, times in sorted(occurrences.items()):
#     print(f"{letter}: {times} time/s")