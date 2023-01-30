rows, cols = [int(x) for x in input().split()]
matrix = [[char for char in input().split()] for row in range(rows)]
occurrences = 0
for r in range(rows - 1):
    for c in range(cols - 1):
        top_left = matrix[r][c]
        top_right = matrix[r][c + 1]
        bottom_left = matrix[r + 1][c]
        bottom_right = matrix[r + 1][c + 1]
        current_char = top_left
        if current_char == top_right \
                and current_char == bottom_left \
                and current_char == bottom_right:
            occurrences += 1
print(occurrences)
