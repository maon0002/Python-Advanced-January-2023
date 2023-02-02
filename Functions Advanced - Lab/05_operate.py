from functools import reduce


def operate(op, *args):
    operand = op
    nums = args
    operations_dict = {
        '+': lambda lst: reduce(lambda x, y: x + y if nums else None, nums),
        '-': lambda lst: reduce(lambda x, y: x - y if nums else None, nums),
        '*': lambda lst: reduce(lambda x, y: x * y if nums else None, nums),
        '/': lambda lst: reduce(lambda x, y: x / y if nums else None, nums),
    }
    result = [(operations_dict[operand](nums))]
    return float(*result)



# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
print(operate("/", 30, 3, 2, 2))

