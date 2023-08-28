#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list and x > 0:
        my_len = 0
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end='')
                my_len += 1
            except IndexError:
                break
        print();
        return my_len
