records = int(input())
result = set()
for _ in range(records):
    username = input()
    result.add(username)

for usrname in result:
    print(usrname)











# names_count = int(input())
# names = set()
#
# for _ in range(names_count):
#     names.add(input())
#
# print(*names, sep="\n")
#
# # one line solution
# # print(*{input() for _ in range(int(input()))}, sep="\n")
