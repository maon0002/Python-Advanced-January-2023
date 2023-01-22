# 5. Truck Tour
# There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive). For each petrol pump, you will receive two pieces of information (separated by a single space):
#     • The amount of petrol the petrol pump will give you
#     • The distance from that petrol pump to the next petrol pump (kilometers)
# You are a truck driver, and you want to go all around the circle. You know that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity.
# In the beginning, the tank is empty, but you start your journey at a petrol pump so you can fill it with the given amount of petrol.
# Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. You never miss filling its tank at a petrol pump.
# Input
#     • On the first line, you will receive the number of petrol pumps - N
#     • On the next N lines, you will receive the amount of petrol that each petrol pump will give and the distance between that petrol pump and the next petrol pump, separated by a single space
# Output
#     • An integer which will be the smallest index of a petrol pump from which you can start the tour
# Constraints
#     • 1 ≤ N ≤ 1000001
#     • You will always have at least one point from where the truck will be able to complete the circle
#     • 1 ≤ amount of petrol, distance ≤ 1000000000
from _collections import deque


# number_of_petrol_pumps = int(input())
# starting_petrol_amount = 0
# pumps_values = {}
# for i in range(number_of_petrol_pumps):
#     petrol, distance = input().split()
#     pumps_values[i] = [int(petrol), int(distance)]

pumps_values = deque([int(x) for x in input().split()] for i in range(int(input())))
# print(f"pumps_chars deque = {pumps_values}")
pumps_values_copy = pumps_values.copy()
idx = None
for i in range(len(pumps_values_copy)):
    # print(*pumps_values_copy[i])
    petrol, distance = pumps_values_copy[i][0], pumps_values_copy[i][1]
    if distance > petrol:
        continue
    elif petrol >= distance:
        idx = i
        break
    # print(petrol, distance)
    # petrol, distance = *[pumps_values_copy[0]]

print(idx)

#dict try
# pumps_chars_dict = {i: [int(x) for x in input().split()] for i in range(int(input()))}
# print('pumps_chars_dict: ', pumps_chars_dict)











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
