rows, cols = [int(n) for n in input().split()]
matrix = [[[] for x in range(cols)] for row in range(rows)]
start = ord("a")

for r in range(rows):
    for c in range(cols):
        string = chr(r + 97) + chr(c + r + 97) + chr(r + 97)
        matrix[r][c].append(string)

for _r in range(rows):
    counter = 0
    for _c in range(cols):
        print(*matrix[_r][_c], end=" ")
        counter += 1
        if counter == cols:
            print()
            break

# [[print(chars[cols]) for chars in range(cols)] for lines in range(rows)]

# print(matrix)

# rows, cols = [int(x) for x in input().split()]
#
# start_end = ord('a')
#
# for row in range(start_end, start_end + rows):
#     for col in range(start_end, start_end + cols):
#         print(f"{chr(row)}{chr((row + col) - start_end)}{chr(row)}", end=" ")
#
#     print()
