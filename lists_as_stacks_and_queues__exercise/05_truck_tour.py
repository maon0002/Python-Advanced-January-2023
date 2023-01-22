from _collections import deque

pumps_data = deque([int(data) for data in input().split()] for i in range(int(input())))
# deque([[1, 5], [10, 3], [3, 4]])
# print(pumps_data)

pumps_data_copy = pumps_data.copy()
fuel = 0
idx = 0

while pumps_data_copy:

    petrol, distance = pumps_data_copy.popleft()
    # print(petrol, distance)
    if (fuel + petrol) - distance < 0:
        moving_el = pumps_data.popleft()
        pumps_data.append(moving_el)
        pumps_data_copy = pumps_data.copy()
        idx += 1
        fuel = 0
    else:
        fuel += petrol - distance

print(idx)








#
# ##lector:
# from _collections import deque
#
# pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
# pumps_data_copy = pumps_data.copy()
#
# index = 0
# gas_in_tank = 0
#
# while pumps_data_copy:
#     petrol, distance = pumps_data_copy.popleft()
#     gas_in_tank += petrol
#
#     if gas_in_tank - distance < 0:
#         pumps_data.rotate(-1)
#         pumps_data_copy = pumps_data.copy()
#
#         index += 1
#         gas_in_tank = 0
#
#     else:
#         gas_in_tank -= distance
#
# print(index)
