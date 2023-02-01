rows, cols = [int(x) for x in input().split()]
matrix = [[c for c in input().split()] for r in range(rows)]
print(matrix)
while True:
    command = [int(n) if n.isdigit() else n for n in input().split()]
    check = [z if z < cols else cols + 1 for z in command[1:]]
    if command[0] == "END":
        break
    elif len(command) != 5 or [x for x in check if x < 0] or [y for y in check if y > cols] or command[0] != "swap":
        print("Invalid input!")
        continue
    elif command[0] == "swap" and cols + 1 not in check:
        row1, col1, row2, col2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
        initial_position = matrix[row1][col1]
        matrix[row1][col1] = matrix[row2][col2]
        matrix[row2][col2] = initial_position
        for row in range(rows):
            print(*[*matrix[row]], sep=" ")
    else:
        break








def check_valid_index(indexes):
    if {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], indexes[3]}.issubset(valid_cols):
        return True

    return False


def swap_command(command, indexes):
    if check_valid_index(indexes) and command == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(matrix[r]) for r in range(rows)], sep="\n")
    else:
        print("Invalid input!")


rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command_type == "END":
        break

    swap_command(command_type, info)