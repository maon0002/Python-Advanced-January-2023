from collections import deque

bees = deque(int(bee) for bee in input().split())
nectar_values = deque(int(nectar) for nectar in input().split())
operations = deque(op for op in input().split())

operations_dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}
honey = 0
while bees and nectar_values:

    current_bee = bees.popleft()
    current_nectar = nectar_values.pop()

    if current_nectar >= current_bee:
        current_operation = operations.popleft()
        honey += (abs(operations_dict[current_operation](current_bee, current_nectar)))

    else:
        bees.appendleft(current_bee)


print(f'Total honey made: {honey}')
if bees:
    print(f"Bees left: {', '.join(str(bee_) for bee_ in bees)}")
if nectar_values:
    print(f"Nectar left: {', '.join(str(nectar_) for nectar_ in nectar_values)}")


#
# from collections import deque
#
# bees = deque(int(x) for x in input().split())
# nectar = deque(int(x) for x in input().split())
# symbols = deque(input().split())
#
# total_honey = 0
#
# operations = {
#     "*": lambda x, y: x * y,
#     "/": lambda x, y: x / y,
#     "-": lambda x, y: x - y,
#     "+": lambda x, y: x + y,
# }
#
# while bees and nectar:
#     curr_bee = bees.popleft()
#     curr_nectar = nectar.pop()
#
#     if curr_nectar < curr_bee:
#         bees.appendleft(curr_bee)
#     elif curr_nectar > curr_bee:
#         total_honey += abs(operations[symbols.popleft()](curr_bee, curr_nectar))
#
# print(f"Total honey made: {total_honey}")
#
# if bees:
#     print(f"Bees left: {', '.join(str(x) for x in bees)}")
#
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
