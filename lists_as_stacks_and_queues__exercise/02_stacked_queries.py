# 2. Stacked Queries
# You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:
#     • '1 {number}' – push the number (integer) into the stack
#     • '2' – delete the number at the top of the stack
#     • '3' – print the maximum number in the stack
#     • '4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"

# number_of_lines = int(input())
stack = list()

functions_dict = {
    1: lambda x: stack.append(x),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}
commands_data = [[int(x) for x in input().split()] for _ in range(int(input()))]
for i in range(len(commands_data)):
    command = commands_data[i][0]
    value = None
    if len(commands_data[i]) > 1:
        value = commands_data[i][1]
    functions_dict[command](value)

print(*reversed(stack), sep=", ")

# print(stack)
# result = [print(stack.pop(), end=", ") for i in range(len(stack))].pop()

# for x in stack:
#     print(x, end=", ")


##lector
# from _collections import deque
#
# numbers = deque()
#
# map_functions = {
#     1: lambda x: numbers.append(x),
#     2: lambda x: numbers.pop() if numbers else None,
#     3: lambda x: print(max(numbers)) if numbers else None,
#     4: lambda x: print(min(numbers)) if numbers else None,
# }
#
# for _ in range(int(input())):
#     numbers_data = [int(x) for x in input().split()]
#     map_functions[numbers_data[0]](numbers_data[1])
#
# numbers.reverse()
#
# print(*numbers, sep=', ')
