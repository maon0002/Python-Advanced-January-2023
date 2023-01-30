rows = int(input())
matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for n in range(rows)]
print(matrix)












# number_of_rows = int(input())
# matrix = []
#
# for _ in range(number_of_rows):
#     current_row = [int(element) for element in input().split(', ') if int(element) % 2 == 0]
#     matrix.append(current_row)
#
# print(matrix)

