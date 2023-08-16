#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum_mul = 0.0
    sum_weight = 0.0
    for i in my_list:
        mul = i[0] * i[1]
        sum_mul += mul
        sum_weight += i[1]
    res = sum_mul / sum_weight
    return res
