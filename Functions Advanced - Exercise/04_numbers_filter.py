def even_odd_filter(**kwargs):
    # even_odd_dict = dict(kwargs)

    result_dict = {}
    for k, v in kwargs.items():
        if k == "odd":
            v = [x for x in v if x % 2 != 0]
        elif k == "even":
            v = [x for x in v if x % 2 == 0]
        if k not in result_dict:
            result_dict[k] = v
        sorted_dict = dict(sorted(result_dict.items(), key=lambda x: -len(x[1])))
    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

















#
# def even_odd_filter(**kwargs):
#     if "odd" in kwargs:
#         kwargs["odd"] = [n for n in kwargs["odd"] if int(n) % 2 == 1]
#
#     if "even" in kwargs:
#         kwargs["even"] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))
#
#     return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
#
#
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))