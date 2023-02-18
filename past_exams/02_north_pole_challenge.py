directions_dict = {
    'up': [-1, 0],  # up
    'down': [1, 0],  # down
    'right': [0, 1],  # right
    'left': [0, -1],  # left
}
all_items = 0
init_rows, init_cols = input().split(", ")
YOU = "Y"
XMAS_DECORATION = "D"
GIFTS = "G"
COOKIES = "C"

your_pos = []
xmas_decor_pos = []
gifts_pos = []
cookies_pos = []
matrix = [[x for x in input().split()] for r in range(int(init_rows))]
# matrix = []
# print(matrix)
for r in range(int(init_rows)):
    for c in range(int(init_cols)):
        el = matrix[r][c]
        if el == YOU:
            your_pos = [r, c]
            matrix[r][c] = "x"
        elif el == XMAS_DECORATION:
            xmas_decor_pos.append([r, c])
            all_items += 1
        elif el == GIFTS:
            gifts_pos.append([r, c])
            all_items += 1
        elif el == COOKIES:
            cookies_pos.append([r, c])
            all_items += 1
collected_dict = {
    "D": 0,
    "G": 0,
    "C": 0,
}
# all_was_collected = None
while all_items:
    command = input().split("-")
    if command[0] == "End":
        break
    direction = command[0]
    value = int(command[1])
    for step in range(value):
        row = your_pos[0] + directions_dict[direction][0]
        col = your_pos[1] + directions_dict[direction][1]
        # curr_position = matrix[row][col]


        if row < 0:
            row = int(init_rows) + row
        elif row > int(init_rows) - 1:
            row = int(init_rows) - row

        if col > int(init_cols) - 1:
            col = int(init_cols) - col
        elif col < 0:
            col = int(init_cols) + col

        pos_check = [row, col]
        if matrix[row][col] == "x":
            your_pos = [row, col]
            continue
        if matrix[row][col] == ".":
            matrix[row][col] = "x"
            your_pos = [row, col]
            continue
        elif matrix[row][col] == XMAS_DECORATION:
            collected_dict[matrix[row][col]] += 1
            all_items -= 1
        elif matrix[row][col] == GIFTS:
            collected_dict[matrix[row][col]] += 1
            all_items -= 1
        elif matrix[row][col] == COOKIES:
            collected_dict[matrix[row][col]] += 1
            all_items -= 1
        # matrix[row][col] = "Y"
        # all_was_collected = all(True if x > 0 else False for x in collected_dict.values())
        if not all_items:
            your_pos = [row, col]
            print("Merry Christmas!")
            break
        matrix[row][col] = "x"
        your_pos = [row, col]
matrix[your_pos[0]][your_pos[1]] = "Y"
# print(matrix)

# if all_was_collected:
#     print("Merry Christmas!")
ITEMS_LIST = ["Christmas decorations", "Gifts", "Cookies"]
print("You've collected:")
print(f"- {collected_dict['D']} Christmas decorations")
print(f"- {collected_dict['G']} Gifts")
print(f"- {collected_dict['C']} Cookies")

for r in range(int(init_rows)):
    print(*matrix[r], sep=" ")


