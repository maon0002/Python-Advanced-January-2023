def concatenate(*args, **kwargs):
    args_concat = "".join(args)
    for k, v in kwargs.items():
        if k in args_concat:
            args_concat = args_concat.replace(k, v)

    return args_concat


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

#
# def concatenate(*args, **kwargs):
#     text = ''.join(args)
#
#     for key in kwargs:
#         text = text.replace(key, kwargs[key])
#
#     return text
