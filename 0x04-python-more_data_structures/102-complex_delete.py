#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    pop_set = set({})
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            pop_set.add(key)
    for ele in pop_set:
        a_dictionary.pop(ele)
    return a_dictionary
