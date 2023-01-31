from collections import deque

size = int(input())
matrix = [[int(x) for x in input().split()] for r in range(size)]
primary_diagonal = list()
secondary_diagonal = list()

range_deque_row = deque(range(0, size))
range_deque_col = deque(reversed(range(0, size)))

while range_deque_col and range_deque_row:
    row = range_deque_row.popleft()
    col = range_deque_col.popleft()
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][col])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))

# num = int(input())
# matrix = [[int(n) for n in input().split()] for row in range(num)]
#
# primary_sum = 0
# secondary_sum = 0
#
# for i in range(num):
#     primary_sum += matrix[i][i]
#     secondary_sum += matrix[num-i-1][i]
#
# print(abs(primary_sum-secondary_sum))
