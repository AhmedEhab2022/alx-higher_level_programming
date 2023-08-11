#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    if len_a == 1:
        x = tuple_a[0]
        y = 0
    elif len_a == 0:
        x = 0
        y = 0
    else:
        x = tuple_a[0]
        y = tuple_a[1]
    if len_b == 1:
        z = tuple_b[0]
        k = 0
    elif len_b == 0:
        z = 0
        k = 0
    else:
        z = tuple_b[0]
        k = tuple_b[1]
    return (x + z, y + k)
