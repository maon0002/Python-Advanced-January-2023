# n_len, m_len = input().split()
# n = set()
# m = set()
#
# for _ in range(int(n_len)):
#     num = int(input())
#     n.add(num)
#
# for _ in range(int(m_len)):
#     num = int(input())
#     m.add(num)
#
# result = n.intersection(m)
# for num in result:
#     print(num)

n, m = [int(x) for x in input().split()]
n_set = {int(input()) for _ in range(n)}
m_set = {int(input()) for _ in range(m)}
print(*n_set.intersection(m_set), sep='\n')



