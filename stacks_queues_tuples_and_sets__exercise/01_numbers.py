first_set = {int(x) for x in input().split()}
second_set = {int(x) for x in input().split()}

commands_dictionary = {
    "Add First": lambda x: [first_set.add(y) for y in x],
    "Add Second": lambda x: [second_set.add(y) for y in x],
    "Remove First": lambda x: [first_set.discard(y) for y in x],
    "Remove Second": lambda x: [second_set.discard(y) for y in x],
    "Check Subset": lambda: print(True) if first_set.issubset(second_set) or second_set.issubset(first_set) else print(False),
}
for i in range(int(input())):
    command = input().split()
    current_command = command[0] + " " + command[1]
    values = [int(x) for x in command if x.isdigit()]
    if current_command in commands_dictionary.keys() and current_command != "Check Subset":
        commands_dictionary[current_command](values)
    else:
        commands_dictionary[current_command]()

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")














# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# functions = {
#     "Add First": lambda x: [first.add(el) for el in x],
#     "Add Second": lambda x: [second.add(el) for el in x],
#     "Remove First": lambda x: [first.discard(n) for n in x],
#     "Remove Second": lambda x: [second.discard(n) for n in x],
#     "Check Subset": lambda: print(True) if first.issubset(second) or second.issubset(first) else print(False)
# }
#
# for _ in range(int(input())):
#     first_command, *data = input().split()
#
#     command = first_command + " " + data.pop(0)
#
#     if data:
#         functions[command]([int(x) for x in data])
#     else:
#         functions[command]()
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")

#====================================================================
#
# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     first_command, *data = input().split()
#
#     command = first_command + " " + data.pop(0)
#
#     if command == "Add First":
#         [first.add(int(el)) for el in data]
#     elif command == "Add Second":
#         [second.add(int(el)) for el in data]
#     elif command == "Remove First":
#         [first.discard(int(n)) for n in data]
#     elif command == "Remove Second":
#         [second.discard(int(n)) for n in data]
#     else:
#         if first.issubset(second) or second.issubset(first):
#             print(True)
#         else:
#             print(False)
#
# print(*sorted(first), sep=", ")
# print(*sorted(second), sep=", ")