rows, cols = [int(n) for n in input().split()]
matrix = []
print(matrix)
start = ord("a")
print(start)

for r in range(rows):
    for c in range(cols):
        # col_i = 97 + r
        string = [chr(r + 97) + chr(c + r + 97) + chr(r + 97)]
        matrix.append(string)

# for r_ in range(rows):
#     for c_ in range(cols):
#         print(*matrix[r_][c_], end="\n")

[[print(*matrix[chars]) for chars in range(cols)] for lines in range(rows)]

print(matrix)

# rows, cols = [int(x) for x in input().split()]
#
# start_end = ord('a')
#
# for row in range(start_end, start_end + rows):
#     for col in range(start_end, start_end + cols):
#         print(f"{chr(row)}{chr((row + col) - start_end)}{chr(row)}", end=" ")
#
#     print()
