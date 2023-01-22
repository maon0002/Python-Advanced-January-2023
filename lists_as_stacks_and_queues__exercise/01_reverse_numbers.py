
# stack = [print(list(char).pop(), end="") for char in list(reversed(input()))]

# input_line = list(reversed(input()))
# print(*input_line, sep="")

input_line = input().split()
reversed_list = list(reversed(input_line))
print(*reversed_list, sep=" ")


# input_line = input().split()
# print(" ".join([list(num).pop() for num in input_line[::-1]]))


# from _collections import deque
#
# text = deque(input().split())
# text.reverse()
#
# print(' '.join(text))
