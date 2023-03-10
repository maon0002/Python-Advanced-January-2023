rows, cols = [int(x) for x in input().split()]
matrix = [[int(n) for n in input().split()] for row in range(rows)]
rows, cols = rows - 2, cols - 2
total = 0
matrix_3x3 = None
for r in range(rows):

    for c in range(cols):

        top_left = matrix[r][c]
        top_mid = matrix[r][c + 1]
        top_right = matrix[r][c + 2]
        mid_left = matrix[r + 1][c]
        mid_mid = matrix[r + 1][c + 1]
        mid_right = matrix[r + 1][c + 2]
        bottom_left = matrix[r + 2][c]
        bottom_mid = matrix[r + 2][c + 1]
        bottom_right = matrix[r + 2][c + 2]
        sum_of_current_3x3 = (
                    top_left + top_mid + top_right + mid_left + mid_mid + mid_right + bottom_left + bottom_mid + bottom_right)
        if sum_of_current_3x3 > total:
            total = sum_of_current_3x3
            matrix_3x3 = f"{top_left} {top_mid} {top_right} \n{mid_left} {mid_mid} {mid_right}\n{bottom_left} {bottom_mid} {bottom_right}"

print(f"Sum = {total}")
print(matrix_3x3)



# rows, cols = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
#
# max_sum = float("-inf")
# biggest_matrix = []
#
# for row in range(rows - 2):
#     for col in range(cols - 2):
#         first_row = matrix[row][col:col+3]
#         second_row = matrix[row+1][col:col+3]
#         third_row = matrix[row+2][col:col+3]
#
#         current_sum = sum(first_row) + sum(second_row) + sum(third_row)
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#             biggest_matrix = [first_row, second_row, third_row]
#
# print(f"Sum = {max_sum}")
# [print(*biggest_matrix[row]) for row in range(3)]