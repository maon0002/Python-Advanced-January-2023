size = int(input())
field = [[int(x) if x.isdigit() else x for x in input().split()] for rows in range(size)]
player_position = []
walls_positions = []
PLAYER = 'P'
WALL = 'X'
path = []

for row in range(size):
    for col in range(size):
        el = field[row][col]
        if el == PLAYER:
            player_position.append([row, col])
            path.append([row, col])
            field[row][col] = 0
        elif el == WALL:
            walls_positions.append([row, col])
print(field)
directions_dict = {
    'up': (-1, 0),  # up
    'down': (1, 0),  # down
    'right': (0, 1),  # right
    'left': (0, -1),  # left
}

print(player_position)
print(walls_positions)
coins = 0
hits_wall = False

while not hits_wall and coins <= 100:
    command = input()

    if command not in directions_dict.keys():
        continue

    row = player_position[0][0]
    col = player_position[0][1]
    x = directions_dict[command][0]
    y = directions_dict[command][1]
    r = row + x
    c = col + y
    if r < 0:
        r = size - 1
    if r == size:
        r = 0
    if c < 0:
        c = size - 1
    if c == size:
        c = 0
    curr_pos = field[r][c]
    if curr_pos == WALL:
        hits_wall = True
        break
    elif curr_pos > 0:
        coins += curr_pos
        field[r][c] = 0

        path.append([r, c])
    else:
        path.append([r, c])
    player_position[0] = [r, c]

print(coins)
print(*path)
