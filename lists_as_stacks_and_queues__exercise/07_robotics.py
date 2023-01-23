






















#
# # 07 first_way

from collections import deque
from datetime import datetime, timedelta

robots = {r.split("-")[0]: [int(r.split("-")[1]), 0] for r in input().split(";")}  # {name: [time_needed, time_for_curr_task]
factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()

while True:
    product = input()

    if product == "End":
        break

    products.append(product)

while products:
    factory_time += timedelta(0, 1)
    product = products.popleft()

    robots = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robots.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))

    if not free_robots:
        products.append(product)
        continue

    robots[free_robots[0][0]][1] = free_robots[0][1][0]

    print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")
#
# # 07 second way
#
# from collections import deque
# from datetime import datetime, timedelta
#
# robots = {}
#
# for r in input().split(";"):
#     name, time_needed = r.split("-")
#     robots[name] = [int(time_needed), 0]
#
# factory_time = datetime.strptime(input(), "%H:%M:%S")
# products = deque()
#
# while True:
#     product = input()
#
#     if product == "End":
#         break
#
#     products.append(product)
#
# while products:
#     factory_time += timedelta(0, 1)
#     product = products.popleft()
#
#     free_robots = []
#
#     for name, value in robots.items():
#         if value[1] != 0:
#             robots[name][1] -= 1
#
#     for name, value in robots.items():
#         if value[1] == 0:
#             free_robots.append([name, value])
#
#     if not free_robots:
#         products.append(product)
#         continue
#
#     robot_name, data = free_robots[0]
#     robots[robot_name][1] = data[0]
#
#     print(f"{free_robots[0][0]} - {product} [{factory_time.strftime('%H:%M:%S')}]")
#
#
