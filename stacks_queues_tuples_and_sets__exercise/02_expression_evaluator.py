











# from _collections import deque
# from functools import reduce
#
# eval_functions = {
#     "*": lambda i: reduce(lambda a, b: int(a) * int(b), map(int, i)),
#     "/": lambda i: reduce(lambda a, b: a / b, map(int, i)),
#     "-": lambda i: reduce(lambda a, b: a - b, map(int, i)),
#     "+": lambda i: reduce(lambda a, b: a + b, map(int, i)),
# }
#
# input_line = deque(input().split())
# input_line_copy = input_line.copy()
#
# operators = ("*", "+", "-", "/")
# calc = []
# while input_line_copy:
#     for char in input_line:
#         validation = input_line_copy.popleft()
#         if validation not in operators:
#             calc.append(int(validation))
#
#         elif validation in operators:
#             calc = [int(eval_functions[validation](calc))]
# print(*calc)





















# from functools import reduce
# from math import floor
#
# expression = input().split()
#
# idx = 0
#
# functions = {
#     "*": lambda i: reduce(lambda a, b: int(a) * int(b), map(int, expression[:i])),
#     "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
#     "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
#     "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
# }
#
# while idx < len(expression):
#     element = expression[idx]
#
#     if element in "*/+-":
#         expression[0] = functions[element](idx)
#         [expression.pop(1) for i in range(idx)]
#         idx = 0
#
#     idx += 1
#
# print(floor(int(expression[0])))

