from collections import deque

pizza_orders = deque(int(n) for n in input().split(", "))
employees = list(int(n) for n in input().split(", "))
total_pizzas = 0

while pizza_orders and employees:
    first_order = pizza_orders.popleft()
    if first_order <= 0:
        if pizza_orders:
            first_order = pizza_orders.popleft()
        else:
            break

    if first_order > 10:
        continue

    last_emp = employees.pop()
    if first_order <= last_emp:
        total_pizzas += first_order
    elif first_order > last_emp:
        first_order -= last_emp
        total_pizzas += last_emp
        pizza_orders.appendleft(first_order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    if employees:
        print(f"Employees: {', '.join(str(x) for x in employees)}")
elif not employees and pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
