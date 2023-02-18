def shop_from_grocery_list(*args):
    budget = args[0]
    need_to_bought = args[1]  # if type[args[0]] == list
    bought_products = []
    for products in args:
        if type(products) == tuple:
            name = products[0]
            price = products[1]
            if name in need_to_bought:
                if budget >= price:
                    bought_products.append(name)
                    need_to_bought.remove(name)
                    budget -= price
                else:
                    break
    if not need_to_bought:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(x for x in need_to_bought)}."





print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
