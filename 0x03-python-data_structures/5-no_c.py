#!/usr/bin/python3
def no_c(my_string):
    for c in my_string:
        if c not in 'cC':
            my_string.remove(c)
    return my_string
