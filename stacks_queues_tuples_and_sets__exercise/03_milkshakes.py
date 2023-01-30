from collections import deque

chocolate = deque([int(choco) for choco in input().split(', ')])
cups_of_milk = deque([int(milk_cups) for milk_cups in input().split(', ')])

milkshakes = 0

while milkshakes < 5 and chocolate and cups_of_milk:
    current_chocolate = chocolate.pop()
    current_milk = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_milk <= 0:
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        chocolate.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        milkshakes += 1
    else:
        cups_of_milk.appendleft(current_milk)
        chocolate.append(current_chocolate - 5)

if milkshakes > 4:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")













from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while milkshakes != 5 and cups_of_milk and chocolates:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")