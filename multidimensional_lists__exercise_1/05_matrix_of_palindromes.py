rows, cols = [int(n) for n in input().split()]
# matrix = [[[]*c for c in range(cols)] for row in range(rows)]
# matrix = [[[] for c in range(cols)] for row in range(rows)]
matrix = []
# [[[], [], [], [], [], []], [[], [], [], [], [], []], [[], [], [], [], [], []], [[], [], [], [], [], []]]
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
# [[['aaa'], ['aba']], [['bab'], ['bbb']], [['cac'], ['cbc']]]