def flights(*args):
    final_dict = {}
    for i in range(len(args)):
        item = args[i]
        if item == "Finish":
            return final_dict
        if type(item) == str:
            if item not in final_dict.keys():
                final_dict[item] = 0
            final_dict[item] += args[i + 1]

    return final_dict


print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))