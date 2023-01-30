from collections import deque

size = int(input())
matrix = [[int(x) for x in input().split(", ")] for r in range(size)]
primary_diagonal = list()
secondary_diagonal = list()

range_deque_row = deque(range(0, size))
range_deque_col = deque(reversed(range(0, size)))

while range_deque_col and range_deque_row:
    row = range_deque_row.popleft()
    col = range_deque_col.popleft()
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][col])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")



# print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))


