sqr_size = int(input())
matrix = [[x for x in input()] for size in range(sqr_size)]
symbol = input()
indexes = None
occurrence_found = False
for row in range(sqr_size):
    for col in range(sqr_size):
        if not occurrence_found:
            char = matrix[row][col]
            if char == symbol:
                indexes = f"({row}, {col})"
                occurrence_found = True

print(indexes) if occurrence_found else print(f"{symbol} does not occur in the matrix")



# def read_matrix_func():
#     number_of_rows = int(input())
#     current_matrix = []
#
#     for row in range(number_of_rows):
#         row_data = list(input())
#         current_matrix.append(row_data)
#
#     return current_matrix
#
#
# def check_func_for_special_symbol(matrix, symbol):
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             current_element = matrix[row][col]
#             if current_element == symbol:
#                 return row, col
#
#
# def print_func(data, symbol):
#     if data:
#         print(data)
#     else:
#         print(f'{symbol} does not occur in the matrix')
#
#
# matrix = read_matrix_func()
# special_symbol = input()
# print_func(check_func_for_special_symbol(matrix, special_symbol), special_symbol)
