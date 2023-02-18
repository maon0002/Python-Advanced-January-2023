size = 7
players = [[x, 501, 0] for x in input().split(", ")]  # [['Ivan', 501], ['Peter', 501]]

matrix = [[int(x) if x.isdigit() else x for x in input().split()]for rows in range(size)]
winner = None
while True:
    curr_player = players[0][0]
    curr_score = players[0][1]
    curr_hit_pos = [int(x) for x in input()[1:-1].split(", ")]
    r, c = curr_hit_pos[0], curr_hit_pos[1]
    if 0 <= r < size and 0 <= c < size:
        curr_hit = matrix[r][c]

        if type(curr_hit) == int:
            players[0][1] -= curr_hit
            players[0][2] += 1

        elif curr_hit == "D":
            r_sum = sum([int(x) for x in matrix[r] if type(x) == int])
            c_sum = 0
            for rows in range(size):
                for cols in range(size):
                    num = matrix[rows][cols]
                    if cols == c and type(num) == int:
                        c_sum += num
            sub_total = (r_sum + c_sum) * 2
            players[0][1] -= sub_total
            players[0][2] += 1
        elif curr_hit == "T":
            r_sum = sum([int(x) for x in matrix[r] if type(x) == int])
            c_sum = 0
            for rows in range(size):
                for cols in range(size):
                    num = matrix[rows][cols]
                    if cols == c and type(num) == int:
                        c_sum += num
            sub_total = (r_sum + c_sum) * 3
            players[0][1] -= sub_total
            players[0][2] += 1
        elif curr_hit == "B":
            winner = players[0][0]
            players[0][2] += 1
            break

    else:
        players[0][2] += 1

    if players[0][1] <= 0:
        winner = players[0][0]
        break

    players[0], players[1] = players[1], players[0]

print(f"{winner} won the game with {players[0][2]} throws!")


#
# size = 7
# players = [[x, 501, 0] for x in input().split(", ")]  # [['Ivan', 501], ['Peter', 501]]
#
# matrix = [[int(x) if x.isdigit() else x for x in input().split()]for rows in range(size)]
# winner = None
# while True:
#     curr_player = players[0][0]
#     curr_score = players[0][1]
#     curr_hit_pos = [int(x) for x in input()[1:-1].split(", ")]
#     r, c = curr_hit_pos[0], curr_hit_pos[1]
#     if 0 <= r < size and 0 <= c < size:
#         curr_hit = matrix[r][c]
#
#         if type(curr_hit) == int:
#             players[0][1] -= curr_hit
#             players[0][2] += 1
#
#         elif curr_hit == "D":
#             r_sum = sum([int(x) for x in matrix[r] if type(x) == int])
#             # c_sum = sum([[int(x) if type(x) == int else 0 for x in matrix[rows][c]]for rows in range(size)])
#             c_sum = 0
#             for rows in range(size):
#                 for cols in range(size):
#                     num = matrix[rows][cols]
#                     if cols == c and type(num) == int:
#                         c_sum += num
#             sub_total = (r_sum + c_sum) * 2
#             players[0][1] -= sub_total
#             players[0][2] += 1
#         elif curr_hit == "T":
#             r_sum = sum([int(x) for x in matrix[r] if type(x) == int])
#             # c_sum = sum([[int(x) if type(x) == int else 0 for x in matrix[rows][c]] for rows in range(size)])
#             c_sum = 0
#             for rows in range(size):
#                 for cols in range(size):
#                     num = matrix[rows][cols]
#                     if cols == c and type(num) == int:
#                         c_sum += num
#             sub_total = (r_sum + c_sum) * 3
#             players[0][1] -= sub_total
#             players[0][2] += 1
#         elif curr_hit == "B":
#             winner = players[0][0]
#             players[0][2] += 1
#             break
#     if players[0][1] <= 0:
#         winner = players[0][0]
#         break
#
#     players[0], players[1] = players[1], players[0]
#
# print(f"{winner} won the game with {players[0][2]} throws!")
