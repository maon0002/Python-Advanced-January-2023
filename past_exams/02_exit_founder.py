players = [[x, 0] for x in input().split(", ")]
size = 6
matrix = [[x for x in input().split()] for y in range(size)]
# print(matrix)
EXIT, TRAP, WALL = "E", "T", "W"
exit_pos = []
traps_pos = []
walls_pos = []
for r in range(size):
    for c in range(size):
        el = matrix[r][c]
        if el == EXIT:
            exit_pos.append([r, c])
        elif el == TRAP:
            traps_pos.append([r, c])
        elif el == WALL:
            walls_pos.append([r, c])


while True:
    curr_player = players[0][0]
    other_player = players[1][0]
    coordinates = [int(x) for x in input()[1:-1].split(", ")]

    if players[0][1]:
        players[0][1] = 0
        players[0], players[1] = players[1], players[0]
        continue

    if coordinates in exit_pos:
        print(f"{players[0][0]} found the Exit and wins the game!")
        break
    elif coordinates in traps_pos:
        print(f"{players[0][0]} is out of the game! The winner is {players[1][0]}.")
        break
    elif coordinates in walls_pos:
        print(f"{players[0][0]} hits a wall and needs to rest.")
        players[0][1] = 1
        player_is_resting = True

    players[0], players[1] = players[1], players[0]










# player_one, player_two = input().split(", ")
# size = 6
# matrix = [[x for x in input().split()] for y in range(size)]
# print(matrix)
# EXIT, TRAP, WALL = "E", "T", "W"
# exit_pos = []
# traps_pos = []
# walls_pos = []
# for r in range(size):
#     for c in range(size):
#         el = matrix[r][c]
#         if el == EXIT:
#             exit_pos.append([r, c])
#         elif el == TRAP:
#             traps_pos.append([r, c])
#         elif el == WALL:
#             walls_pos.append([r, c])
#         # matrix[r][c] = "."
# print(walls_pos)
# player_is_resting = False
# players = [player_one, player_two]
# turn = 0
#
# # players_dict = {}
# # for p in players:
# #     if p not in players_dict.keys():
# #         players_dict[p] = []
#
# players_dict = [[x, []] for x in players]
# curr_player = players_dict[0][0]
# other_player = players_dict[1][0]
# curr_player_status = players_dict[0][1]
# other_player_status = players_dict[1][1]
# while True:
#
#     coordinates = [int(x) for x in input()[1:-1].split(", ")]
#
#     print(curr_player)
#     print(other_player)
#
#     if players_dict[0][1]:
#         players_dict[0][1] = []
#         continue
#
#     if coordinates in exit_pos:
#         print(f"{players_dict[0][0]} found the Exit and wins the game!")
#         break
#     elif coordinates in traps_pos:
#         print(f"{players_dict[0][0]} is out of the game! The winner is {players_dict[1][0]}.")
#         break
#     elif coordinates in walls_pos:
#         print(f"{players_dict[0][0]} hits a wall and needs to rest.")
#         players_dict[1].append(True)
#         player_is_resting = True
#
#     # players[0], players[1] = players[1], players[0]
#     players_dict[0][0], players_dict[1][0] = players_dict[1][0], players_dict[0][0]