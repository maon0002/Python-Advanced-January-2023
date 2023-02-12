size = int(input())
matrix = [[x for x in input()] for row in range(size)]
# print(matrix)
mines_positions = []
submarine_position = []
cruiser_positions = []
SUBMARINE = 'S'
MINES = '*'
CRUISER = 'C'
EMPTY = "-"
hit_mines = 0
s_path = []
for row in range(size):
    for col in range(size):
        element = matrix[row][col]
        if element == SUBMARINE:
            submarine_position.append([row, col])
            matrix[row][col] = "-"
        elif element == MINES:
            mines_positions.append([row, col])
        elif element == CRUISER:
            cruiser_positions.append([row, col])

# print(submarine_position)
# print(mines_positions)
# print(cruiser_positions)
directions_dict = {
    'up': (-1, 0),  # up
    'down': (1, 0),  # down
    'right': (0, 1),  # right
    'left': (0, -1),  # left
}

while hit_mines < 3 and cruiser_positions:
    command = input()
    s_curr_pos = submarine_position.pop()

    s_row = s_curr_pos[0]
    s_col = s_curr_pos[1]
    # s_path.append([s_row, s_col])

    curr_direction = directions_dict[command]
    d_row = curr_direction[0]
    d_col = curr_direction[1]
    r_move = s_row + d_row
    c_move = s_col + d_col
    s_path.append([r_move, c_move])
    # TODO append submarine_position
    # if matrix[r_move][c_move] ==
    if [r_move, c_move] in mines_positions:
        matrix[r_move][c_move] = "-"
        hit_mines += 1
        mines_positions.remove([r_move, c_move])
        if hit_mines == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r_move}, {c_move}]!")
            # s_path.pop()
            break
    elif [r_move, c_move] in cruiser_positions:
        matrix[r_move][c_move] = "-"
        cruiser_positions.remove([r_move, c_move])
        if not cruiser_positions:
            print(f"Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

            break
    submarine_position.append([r_move, c_move])

last_row, last_col = s_path[-1]
# print(s_path)
# print(last_row, last_col)
matrix[s_path[-1][0]][s_path[-1][1]] = SUBMARINE
# print(*matrix, sep="\n")

for r in range(size):
    print(*matrix[r], sep="")