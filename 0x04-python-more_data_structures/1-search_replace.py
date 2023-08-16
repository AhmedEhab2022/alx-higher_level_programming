#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        cp_list = my_list.copy()
        for i in range(len(cp_list)):
            if cp_list[i] == search:
                cp_list[i] = replace
        return cp_list
