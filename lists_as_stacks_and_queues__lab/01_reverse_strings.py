#     1. Reverse Strings
# Write program that:
#     • Reads an input string
#     • Reverses it using a stack
#     • Prints the result back on the console

stack = list(input())

while stack:
    print(stack.pop(), end='')
