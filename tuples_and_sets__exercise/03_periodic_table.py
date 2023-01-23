records = int(input())
result = set()
for i in range(records):
    elements = input().split()
    for x in elements:
        result.add(x)
print(*result, sep='\n')









# elements = set()
#
# for _ in range(int(input())):
#     for el in input().split():
#         elements.add(el)
#
# print(*elements, sep="\n")