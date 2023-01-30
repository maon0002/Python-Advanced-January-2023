rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(n) for n in input().split(", ")]for r in range(rows)]
matrix_2x2 = None
total = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        left_top = matrix[row][col]
        right_top = matrix[row][col + 1]
        left_bottom = matrix[row + 1][col]
        right_bottom = matrix[row + 1][col + 1]
        current_sqr_sum = left_bottom + left_top + right_bottom + right_top
        if current_sqr_sum > total:
            total = current_sqr_sum
            matrix_2x2 = f"{left_top} {right_top}\n{left_bottom} {right_bottom}"

print(matrix_2x2)
print(total)
















# def read_matrix():
#     data = input().split(', ')
#     size = int(data[0])
#     matrix = []
#
#     for _ in range(size):
#         row_data = list(map(int, input().split(', ')))
#         matrix.append(row_data)
#
#     return matrix
#
#
# def submatrix_sum_func(matrix, row_index, column_index, matrix_size):
#     total_sum = 0
#     for row in range(row_index, row_index + matrix_size):
#         for col in range(column_index, column_index + matrix_size):
#             total_sum += matrix[row][col]
#
#     return total_sum
#
#
# def get_data_for_best_submatrix(matrix, size_of_submatrix):
#     current_largest_row_index = 0
#     current_largest_column_index = 0
#     best_total_sum = submatrix_sum_func(matrix, 0, 0, size_of_submatrix)
#
#     for row_index in range(len(matrix) - size_of_submatrix + 1):
#         for col_index in range(len(matrix[row_index]) - size_of_submatrix + 1):
#             current_sum = submatrix_sum_func(matrix, row_index, col_index, size_of_submatrix)
#
#             if current_sum > best_total_sum:
#                 best_total_sum = current_sum
#                 current_largest_row_index = row_index
#                 current_largest_column_index = col_index
#
#     return current_largest_row_index, current_largest_column_index
#
#
# def print_function(submatrix_data, size):
#     row_index, column_index = submatrix_data
#     for row in range(row_index, row_index + size):
#         data = []
#         for col in range(column_index, column_index + size):
#             data.append(matrix[row][col])
#         print(' '.join(str(x) for x in data))
#     print(submatrix_sum_func(matrix, row_index, column_index, size))
#
#
# matrix = read_matrix()
# size_of_submatrix = 2
# submatrix_data = get_data_for_best_submatrix(matrix, size_of_submatrix)
# print_function(submatrix_data, size_of_submatrix)
