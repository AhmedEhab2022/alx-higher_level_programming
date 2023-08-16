#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    if my_list:
        s = set(my_list)
        for num in s:
            res += num
    return res
