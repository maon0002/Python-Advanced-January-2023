# Write a program that reads a string with N integers from the console, separated by a single space, and reverses them using a stack. Print the reversed integers on one line, separated by a single space.

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
