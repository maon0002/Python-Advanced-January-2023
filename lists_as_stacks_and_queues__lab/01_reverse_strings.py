
stack = list(input())

while stack:
    print(stack.pop(), end='')

##one line submissions
# input_line = [print(char, end='') for char in input()[::-1]]
# input_line = [print(char, end='') for char in reversed(input())]
# input_line = [print(list(char).pop(), end='') for char in list(reversed(input()))]



