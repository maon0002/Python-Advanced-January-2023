# unique_names = {{print(name) for name in input()} for _ in range(int(input()))}
records = int(input())

unique_names = {input() for _ in range(int(input()))}
print(*unique_names, sep='\n')







# n = int(input())
# names_data = {input() for _ in range(n)}
#
# for name in names_data:
#     print(name)