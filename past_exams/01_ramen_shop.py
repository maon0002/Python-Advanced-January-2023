from collections import deque

ramen = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))

while ramen and customers:
    curr_ramen = ramen.pop()
    curr_customer = customers.popleft()
    diff = None
    if curr_customer == curr_ramen:
        continue
    elif curr_ramen > curr_customer:
        diff = curr_ramen - curr_customer
        ramen.append(diff)
    elif curr_customer > curr_ramen:
        diff = curr_customer - curr_ramen
        customers.appendleft(diff)

if not customers:
    print(f"Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    if customers:
        print(f"Customers left: {', '.join(str(x) for x in customers)}")