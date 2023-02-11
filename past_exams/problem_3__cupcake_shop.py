# from _collections import deque


def stock_availability(inventory, *delivery_or_sell):
    command = delivery_or_sell[0]
    new_inventory_list = inventory
    if command == "delivery":
        additional_products = list(x for x in delivery_or_sell[1:])
        new_inventory_list.extend(additional_products)
    elif command == 'sell':

        if len(delivery_or_sell) == 1:
            new_inventory_list.pop(0)
        elif type(delivery_or_sell[1]) == int:
            for n in range(delivery_or_sell[1]):
                new_inventory_list.pop(0)
        else:
            sold_flavour = delivery_or_sell[1]
            if sold_flavour in new_inventory_list:
                # [new_inventory_list.remove(sold_flavour) for x in new_inventory_list if x == sold_flavour]
                # new_inventory_list = filter(new_inventory_list, lambda x: x != sold_flavour)
                new_inventory_list = [x for x in new_inventory_list if x != sold_flavour]

    return new_inventory_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
