directions = {
    'up': [-1, 0],  # up
    'down': [1, 0],  # down
    'right': [0, 1],  # right
    'left': [0, -1],  # left
}
size = [int(x) for x in input().split()]
rows = size[0]
cols = size[1]
matrix = [[x for x in input().split()] for _ in range(rows)]
my_pos = None
for row in range(rows):
    for col in range(cols):
        el = matrix[row][col]
        if el == "B":
            my_pos = [row, col]
            matrix[row][col] = "-"
            # print(my_pos)

PLAYERS_QTY = 3
moves = 0
touched_players = 0

while True:
    command = input()
    if command == "Finish":
        break

    r = my_pos[0] + directions[command][0]
    c = my_pos[1] + directions[command][1]
    if 0 <= r < rows and 0 <= c <cols and matrix[r][c] != "O":
        if matrix[r][c] == "-":
            moves += 1
            my_pos = [r, c]
        elif matrix[r][c] == "P":
            moves += 1
            my_pos = [r, c]
            touched_players += 1
            matrix[r][c] = "-"
    if touched_players == PLAYERS_QTY:
        break

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves}")












# directions_dict = {
#     'up': (-1, 0),  # up
#     'down': (1, 0),  # down
#     'right': (0, 1),  # right
#     'left': (0, -1),  # left
# }
#
# ME = "B"
# OBSTACLES = "O"
# OTHER_PLAYERS = "P"
# PLAYERS_NUMBER = 3
# me_pos = []
# other_player_pos = []
# obstacle_pos = []
#
# rows, cols = input().split()
# matrix = [[x for x in input().split()] for row in range(int(rows))]
#
# for row in range(int(rows)):
#     for col in range(int(cols)):
#         el = matrix[row][col]
#         if el == ME:
#             me_pos = [row, col]
#         elif el == OBSTACLES:
#             obstacle_pos.append([row, col])
#         elif el == OTHER_PLAYERS:
#             other_player_pos.append([row, col])
#
# touched_opponents = 0
# moves_counter = 0
#
# while touched_opponents < PLAYERS_NUMBER:
#     command = input()
#     if command == "Finish":
#         break
#     r = me_pos[0] + directions_dict[command][0]
#     c = me_pos[1] + directions_dict[command][1]
#     if 0 <= r < int(rows) and 0 <= c < int(cols):
#         if matrix[r][c] == OBSTACLES:
#             continue
#
#         elif matrix[r][c] == OTHER_PLAYERS:
#             moves_counter += 1
#             touched_opponents += 1
#             matrix[r][c] = "-"
#             me_pos = [r, c]
#
#         elif matrix[r][c] == "-":
#             moves_counter += 1
#             me_pos = [r, c]
#
# print("Game over!")
# print(f"Touched opponents: {touched_opponents} Moves made: {moves_counter}")
