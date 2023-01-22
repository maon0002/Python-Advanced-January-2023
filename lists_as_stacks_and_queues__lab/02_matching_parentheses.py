

input_line = input()
indexes = []

for i in range(len(input_line)):
    char = input_line[i]

    if char == '(':
        indexes.append(i)
    elif char == ')':
        to_index = i + 1
        print(input_line[indexes.pop():to_index])

