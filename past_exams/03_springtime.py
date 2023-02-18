def start_spring(**kwargs):
    print(kwargs)
    new_kwargs_dict = {}
    for x in kwargs.items():
        name = x[0]
        type = x[1]
        if type not in new_kwargs_dict.keys():
            new_kwargs_dict[type] = []
        new_kwargs_dict[type].append(name)
    print(new_kwargs_dict)
    sorted_dict = sorted(new_kwargs_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    print(sorted_dict)
    output = []
    for i in range(len(sorted_dict)):
        current_type = sorted_dict[i][0]
        type_to_add = f"{current_type}:"
        output.append(type_to_add)
        if sorted_dict[i][1]:
            sorted_names = sorted(sorted_dict[i][1])
            for names in sorted_names:
                name_to_add = f"-{names}"
                output.append(name_to_add)
    return "\n".join(x for x in output)







example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))


#
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
#
#
#
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
