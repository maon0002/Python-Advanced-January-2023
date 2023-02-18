size = 8
directions = {
    "w": (
        [-1, -1],  # upleft
        [-1, 1],  # upright
        [-1, 0],),  # up

    "b": (
        [1, -1],  # upleft
        [1, 1],  # upright
        [1, 0],)  # up
}

chess_table = []
for num in range(8, 0, -1):
    row = 8 - num
    for letter in range(97, 105):
        col = letter - 97
        chess_table.append([chr(letter) + str(num),[row, col]])

# print(chess_table)
players = ["w", "b"]

matrix = [[] for x in range(size)]
WHITE_PAWN = "w"
BLACK_PAWN = "b"
w_pawn_pos = None
b_pawn_pos = None

for row in range(size):
    col_counter = 0
    for el in input().split():
        matrix[row].append(el)
        if el == "-":
            col_counter += 1
            continue
        elif el == WHITE_PAWN:
            w_pawn_pos = [row, col_counter]
        elif el == BLACK_PAWN:
            b_pawn_pos = [row, col_counter]
# print(matrix)
both_players_pos = [w_pawn_pos, b_pawn_pos]
winner = None
win_pos = None
queen = None

while not queen and not win_pos:
    curr_player = players[0]
    curr_row = both_players_pos[0][0]
    curr_col = both_players_pos[0][1]

    for i in range(3):
        r = curr_row + directions[curr_player][i][0]
        c = curr_col + directions[curr_player][i][1]
        if 0 <= c < size:
            if matrix[r][c] == players[1]:
                winner = curr_player
                win_pos = [r, c]
                break
            elif r in (0, size - 1) and i == 2:
                queen = players[0]
                winner = curr_player
                win_pos = [r, c]
                break
            elif i == 2:
                both_players_pos[0] = [r, c]
        else:
            continue

    if not win_pos:
        both_players_pos[0], both_players_pos[1] = both_players_pos[1], both_players_pos[0]
        players[0], players[1] = players[1], players[0]
    else:
        break
winner_color = "White" if winner is WHITE_PAWN else "Black"
win_chess_position = [x[0] for x in chess_table if win_pos in x]

if not queen:
    print(f"Game over! {winner_color} win, capture on {''.join(x for x in win_chess_position)}.")
else:
    print(f"Game over! {winner_color} pawn is promoted to a queen at {''.join(x for x in win_chess_position)}.")








#
#
#
# size = 8
# directions = {
#     "w": (
#         [-1, -1],  # upleft
#         [-1, 1],  # upright
#         [-1, 0],),  # up
#
#     "b": (
#         [1, -1],  # upleft
#         [1, 1],  # upright
#         [1, 0],)  # up
# }
#
# chess_table = []
# for num in range(8, 0, -1):
#     row = 8 - num
#     for letter in range(97, 105):
#         col = letter - 97
#         chess_table.append([chr(letter) + str(num),[row, col]])
#
# print(chess_table)
# players = ["w", "b"]
#
# matrix = [[] for x in range(size)]
# WHITE_PAWN = "w"
# BLACK_PAWN = "b"
# w_pawn_pos = None
# b_pawn_pos = None
#
# for row in range(size):
#     col_counter = 0
#     for el in input().split():
#         matrix[row].append(el)
#         if el == "-":
#             col_counter += 1
#             continue
#         elif el == WHITE_PAWN:
#             w_pawn_pos = [row, col_counter]
#         elif el == BLACK_PAWN:
#             b_pawn_pos = [row, col_counter]
# print(matrix)
# both_players_pos = [w_pawn_pos, b_pawn_pos]
# winner = None
# win_pos = None
# queen = None
#
# while True:
#     curr_player = players[0]
#     curr_row = both_players_pos[0][0]
#     curr_col = both_players_pos[0][1]
#
#     for i in range(3):
#         r = curr_row + directions[curr_player][i][0]
#         c = curr_col + directions[curr_player][i][1]
#         if (0 <= r < size) and (0 <= c < size):
#             if i == 2:
#                 both_players_pos[0] = [r, c]
#                 continue
#             elif matrix[r][c] == players[1]:
#                 winner = curr_player
#                 win_pos = [r, c]
#                 break
#         elif 0 >= c >= size:
#             continue
#         elif r == 0 or r == size:
#             queen = players[0]
#             win_pos = [r, c]
#             break
#
#     if not winner:
#         both_players_pos[0], both_players_pos[1] = both_players_pos[1], both_players_pos[0]
#         players[0], players[1] = players[1], players[0]
#     else:
#         break
# winner_color = "White" if winner is WHITE_PAWN else "Black"
# win_chess_position = [x[0] for x in chess_table if win_pos in x]
#
# if not queen:
#     print(f"Game over! {winner_color} win, capture on {''.join(x for x in win_chess_position)}.")
# else:
#     print(f"Game over! {winner_color} pawn is promoted to a queen at {''.join(x for x in win_chess_position)}.")
#
#
