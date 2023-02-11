from sys import maxsize

size = 6
matrix = list()
gift_dict = {
    'Football': range(100, 199 + 1),
    'Teddy Bear': range(200, 299 + 1),
    'Lego Construction Set': range(300, maxsize),
}
BUCKET = 'B'
THROWS = 3

b_positions = list()
for row in range(0, size):
    curr_row = [int(n) if n.isdigit() else n for n in input().split()]
    for col in range(len(curr_row)):
        symbol = curr_row[col]
        if symbol == BUCKET:
            b_positions.append([row, col])
    curr_row = [x if type(x) == int else 0 for x in curr_row]
    matrix.append(curr_row)


# print(matrix)
# print(b_positions)

coordinates = {tuple(int(xy) for xy in (input()[1:-1]).split(", ") if xy.isdigit()) for throw in range(THROWS)}

# print(coordinates)


col_sum_dict = {}
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        col_i_value = matrix[r][c]
        if c not in col_sum_dict.keys():
            col_sum_dict[c] = 0
        col_sum_dict[c] += col_i_value
# print(col_sum_dict)

got_prize = False
total_score = 0
gifts_list = None


for xyz in coordinates:
    xyz = [xyz[0], xyz[1]]
    if xyz in b_positions:
        total_score += col_sum_dict[xyz[1]]
        continue

for item in gift_dict.items():
    name = item[0]
    cost = item[1]
    if total_score in cost:
        got_prize = True
        gifts_list = name

if got_prize:
    print(f"Good job! You scored {total_score} points, and you've won {gifts_list}.")
else:
    print(f"Sorry! You need {abs(total_score - 100)} points more to win a prize.")