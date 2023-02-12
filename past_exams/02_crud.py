matrix = [[x for x in input().split()]for row in range(6)]
# print(matrix)
first_position = list([int(x)for x in input() if x.isdigit()])
# print(first_position)

directions_dict = {
    'up': (-1, 0),  # up
    'down': (1, 0),  # down
    'right': (0, 1),  # right
    'left': (0, -1),  # left
}

while True:
    command = input().split(", ")
    if command[0] == "Stop":

        break

    crud = command[0]
    direction = command[1]
    r, c = first_position[0] + directions_dict[direction][0], first_position[1] + directions_dict[direction][1]

    if crud == "Create":
        value = command[2]
        if matrix[r][c] == ".":
            matrix[r][c] = value
    elif crud == "Update":
        value = command[2]
        if matrix[r][c] != ".":
            matrix[r][c] = value
    elif crud == "Delete":
        if matrix[r][c] != ".":
            matrix[r][c] = "."
    elif crud == "Read":
        if matrix[r][c] != ".":
            print(matrix[r][c])
    first_position = [r, c]
for r in range(6):
    print(' '.join(matrix[r]))