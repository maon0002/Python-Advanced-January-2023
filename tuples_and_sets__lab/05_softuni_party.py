records = int(input())
regulars = set()
vips = set()

for _ in range(records):
    reservation_code = input()
    # begins_with = reservation_code[0]
    if reservation_code[0].isdigit():
        vips.add(reservation_code)
    else:
        regulars.add(reservation_code)

did_come = set()
while True:
    command = input()

    if command == "END":
        break
    did_come.add(command)

result = list(vips.difference(did_come))
result.extend(regulars.difference(did_come))
print(len(result))

for code in sorted(result):
    print(code)













# def collect_data_for_arrived_guests():
#     arrived_guests_list = []
#     while True:
#         data = input()
#         if data == 'END':
#             break
#         else:
#             arrived_guests_list.append(data)
#
#     return arrived_guests_list
#
#
# def print_func(not_arrived_guests_data):
#     print(len(not_arrived_guests_data))
#     for guest_number in sorted(not_arrived_guests_data):
#         print(guest_number)
#
#
# n = int(input())
# guest_reservation_list = [input() for _ in range(n)]
# arrived_guests = collect_data_for_arrived_guests()
# not_arrived_guests = set(guest_reservation_list).difference(arrived_guests)
# print_func(not_arrived_guests)