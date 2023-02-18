def shopping_list(budget,**kwargs):
    budget_calc = budget
    finished_orders = []
    if budget > 99:

        for products in kwargs.items():
            name = products[0]
            price = products[1][0]
            qty = products[1][1]
            current_order_total = price * qty
            if current_order_total <= budget_calc:
                if len(finished_orders) < 5:
                    budget_calc -= current_order_total
                    shopping_line_to_add = f"You bought {name} for {current_order_total:.2f} leva."
                    finished_orders.append(shopping_line_to_add)
                else:
                    break
        return "\n".join(x for x in finished_orders)

    else:
        return "You do not have enough budget."








# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
