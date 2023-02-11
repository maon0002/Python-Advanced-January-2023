size = 8
matrix = [[x for x in input().split()] for r in range(size)]
KING = 'K'
QUEEN = 'Q'
k_position = None
q_positions = []
is_king_safe = True

for r in range(len(matrix)):
    for c in range(len(matrix)):
        el = matrix[r][c]
        if el == KING:
            k_position = [r, c]
        elif el == QUEEN:
            q_positions.append([r, c])

q_directions = (
    (-1, 0),  # up
    (1, 0),  # down
    (0, 1),  # right
    (0, -1),  # left
    (-1, -1),  # upleft
    (1, -1),  # downleft
    (-1, 1),  # upright
    (1, 1),  # downright
)

# print(matrix)
# print(k_position)
# print(q_positions)

capture_queen_positions = []

while q_positions:
    curr_queen_pos = q_positions.pop()  # 7, 3
    row, col = curr_queen_pos  # 7, 3

    for x, y in q_directions:  # (-1, 0),

        for i in range(1, size):
            r = row + (x * i)
            c = col + (y * i)

            if 0 <= r < len(matrix) and 0 <= c < len(matrix):
                current_position = matrix[r][c]
                if current_position == QUEEN:
                    break
                elif current_position == KING:
                    capture_queen_positions.append(curr_queen_pos)
                    is_king_safe = False
                    break

    # for direction, positions in directions.items():  # развъртаме цикъл за всяка посока и нейните позиции
    #     row, col = [  # запазваме новата позиция, като събираме текущата позиция с тази от речника
    #         bunny_pos[0] + positions[0],
    #         bunny_pos[1] + positions[1]
    #     ]
    #     path = []  # създаваме променлива, в която да пазим текущия път
    #     collected_eggs = 0  # създаваме променлива, в която да пазим броя на събраните яйца за текущата посока
    #
    #     while 0 <= row < size and 0 <= col < size:  # развъртаме цикъл с условие докато позицията на яйцето е валидна
    #         if matrix[row][col] == 'X':  # проверяваме дали имаме капан на текущата позиция
    #             break  # прекратяваме цикъла
    #
    #         collected_eggs += int(matrix[row][col])  # събираме яйцата на текущата позиция с текущите яйца
    #         path.append([row, col])  # добавяме текущата позиция към текущия път
    #
    #         row += positions[0]  # събираме текущия ред с реда от посоката, в която се движим
    #         col += positions[1]  # събираме текущата колона с колоната от посоката, в която се движим

print(*capture_queen_positions, sep="\n") if not is_king_safe else print("The king is safe!")
