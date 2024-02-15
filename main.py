# ********************** FIRST EXAMPLE *******
# def printing(func):
#     def inner(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'func {func} called with result: {result}')
#         return result
#     return inner
#
#
# @printing
# def add_one(x):
#     return x + 1
#
#
# y = add_one(10)
# print(y)

# ********************** SECOND EXAMPLE *******

import random


def my_decorator(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        result_int = int(result)
        return result_int

    return inner


@my_decorator
def get_rand_number():
    return random.randint(100, 200) / random.randint(1, 100)


print(get_rand_number())
