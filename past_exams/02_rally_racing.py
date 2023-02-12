directions_dict = {
    'up': (-1, 0),  # up
    'down': (1, 0),  # down
    'right': (0, 1),  # right
    'left': (0, -1),  # left
}

size = int(input())
racing_number = input()
matrix = [[x for x in input().split()] for row in range(size)]
car_initial_coordinates = [[0, 0]]
distance = 0
TUNNEL = 'T'
FINNISH = 'F'
DEFAULT_DISTANCE_KM = 10

tunnel_pos = []
finnish_pos = []
# no_action_pos = []

for row in range(size):
    for col in range(size):
        element = matrix[row][col]
        if element == TUNNEL:
            tunnel_pos.append([row,col])
            # matrix[row][col] = "."
        elif element == FINNISH:
            finnish_pos.append([row,col])


# print(matrix)
car_path = car_initial_coordinates
car_finnished = False

while True:
    command = input()
    if command == 'End':
        if not car_finnished:
            print(f"Racing car {racing_number} DNF.")
            break
        break
    curr_r_pos, curr_c_pos = car_path[-1]
    # print(curr_r_pos,curr_c_pos)
    row_move = curr_r_pos + directions_dict[command][0]
    col_move = curr_c_pos + directions_dict[command][1]

    car_path.append([row_move, col_move])
    # print(tunnel_pos[0], "tunnel")
    # print([row_move, col_move],"car")
    if [row_move, col_move] in tunnel_pos:
        distance += DEFAULT_DISTANCE_KM * 3
        entry_tunnel = tunnel_pos[0]
        exit_tunnel = tunnel_pos[1]
        car_path.append(exit_tunnel)
        matrix[row_move][col_move] = "."
        matrix[exit_tunnel[0]][exit_tunnel[1]] = "."
    elif [row_move, col_move] in finnish_pos:
        distance += DEFAULT_DISTANCE_KM
        print(f"Racing car {racing_number} finished the stage!")
        car_finnished = True
        # car_path
        break
    else:
        distance += DEFAULT_DISTANCE_KM

# if car_finnished:
#     print(f"Racing car {racing_number} finished the stage!")
print(f"Distance covered {distance} km.")

# print(car_path)
matrix[car_path[-1][0]][car_path[-1][1]] = "C"

for row in range(size):
    print("".join(matrix[row]))


