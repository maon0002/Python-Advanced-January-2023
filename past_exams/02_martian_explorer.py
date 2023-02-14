from collections import deque

directions_dict = {
    'up': (-1, 0),  # up
    'down': (1, 0),  # down
    'right': (0, 1),  # right
    'left': (0, -1),  # left
}
size = 6
matrix = [[x for x in input().split()] for i in range(size)]

one_rover_pos = []
water_pos = []
metal_pos = []
concrete_pos = []
rock_pos = []
ROVER, WATER, METAL, CONCRETE, ROCK = "E", "W", "M", "C", "R"
for r in range(size):
    for c in range(size):
        el = matrix[r][c]
        if el == ROVER:
            one_rover_pos = [r, c]
        elif el == WATER:
            water_pos.append([r, c])
        elif el == METAL:
            metal_pos.append([r, c])
        elif el == CONCRETE:
            concrete_pos.append([r, c])
        elif el == ROCK:
            rock_pos.append([r, c])

commands = deque(x for x in input().split(", "))
is_broken = False
area_dict = {
    "W": 0,
    "M": 0,
    "C": 0, }
area_is_suitable = None
while commands and not is_broken:
    command = commands.popleft()
    row = one_rover_pos[0] + directions_dict[command][0]
    col = one_rover_pos[1] + directions_dict[command][1]
    if row < 0:
        row = size + row
    elif row > size - 1:
        row = size - row

    if col > size - 1:
        col = size - col
    elif col < 0:
        col = size + col
    curr_pos = [row, col]

    if matrix[row][col] == "-":
        one_rover_pos = curr_pos
        continue
    if matrix[row][col] == ROCK:
        is_broken = True
        print(f"Rover got broken at ({row}, {col})")
        break
    if curr_pos in water_pos:
        area_dict["W"] += 1
        print(f"Water deposit found at ({row}, {col})")
    elif curr_pos in metal_pos:
        area_dict["M"] += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif curr_pos in concrete_pos:
        area_dict["C"] += 1
        print(f"Concrete deposit found at ({row}, {col})")

    one_rover_pos = curr_pos

    area_is_suitable = all(True if x > 0 else False for x in area_dict.values())

# print(area_is_suitable)

if area_is_suitable:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

