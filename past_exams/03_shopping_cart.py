def shopping_cart(*args):
    ref_dict = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }
    shopping_dict = {}

    for pair in args:
        if "Stop" in pair:
            break

        if type(pair) == tuple:
            meal = pair[0]
            if meal not in shopping_dict.keys():
                shopping_dict[meal] = []
            if len(pair) == 1:
                continue
            else:
                if len(shopping_dict[meal]) < ref_dict[meal]:
                    product = pair[1]
                    if product not in shopping_dict[meal]:
                        shopping_dict[meal].append(product)
        else:
            meal = pair
            if meal not in shopping_dict.keys():
                shopping_dict[meal] = []

    print(shopping_dict)
    sorted_dict = sorted(shopping_dict.items(), key=lambda x: (-len(x[1]), x[0], x[1]))

    print(sorted_dict)
    if sorted_dict:
        final_list = []
        for i in range(len(sorted_dict)):
            meal_name = sorted_dict[i][0]
            final_list.append(f"{meal_name}:")
            for product in sorted(sorted_dict[i][1]):
                final_list.append(f" - {product}")
        return "\n".join(x for x in final_list)
    return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'ham'),
    ('Pizza', 'flour'),
    ('Dessert'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
#
#
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
#
#
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))


#
# def shopping_cart(*args):
#     ref_dict = {
#         'Soup': 3,
#         'Pizza': 4,
#         'Dessert': 2,
#     }
#     shopping_dict = {}
#
#     for i in range(len(args)):
#         print(args[i])
#         for x in args[i]:
#             meal, product = x[0], x[1]
#             print(meal)
#             print(product)
#             if meal not in shopping_dict.keys():
#                 shopping_dict[meal] = []
#             if len(shopping_dict[meal]) < ref_dict[meal]:
#                 shopping_dict[meal].append(product)
#     print(shopping_dict)
#     return None
