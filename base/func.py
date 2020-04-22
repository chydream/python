# lambda()
# filter(func,seq)
# map(func,seq)
# reduce(func, seq)
from functools import reduce


def use_filter():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rest = filter(lambda n: n % 2 != 0, l)
    print(rest)
    print(list(rest))
use_filter()

def pow_number():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rest_list = []
    for x in l:
        rest_list.append(x*x*x)
    print(rest_list)
    return rest_list
pow_number()

def pow_num_use_map():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    r = map(lambda x: x*x*x, l)
    print(r)
    print(list(r))
pow_num_use_map()

def get_sum():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    r = reduce(lambda n, m:n+m, l)
    print(r)
get_sum()