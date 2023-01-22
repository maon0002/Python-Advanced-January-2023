from _collections import deque

food_qty = int(input())
orders = deque(int(order) for order in input().split())
print(max(orders))

for order_in_queue in orders.copy():
    if order_in_queue <= food_qty:
        orders.popleft()
        food_qty -= order_in_queue
    else:
        break
print("Orders complete") if not orders else print(
    f"Orders left: {' '.join([str(orders_left) for orders_left in orders])}")



##lector:
#
# from _collections import deque
#
# food = int(input())
# orders = deque([int(n) for n in input().split()])
#
# for order in orders.copy():
#     if food - order >= 0:
#         orders.popleft()
#         food -= order
#     else:
#         print(f"Orders left {' '.join([str(o) for o in orders])}")
#         break
# else:
#     print("Orders complete")
