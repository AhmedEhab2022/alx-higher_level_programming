#!/usr/bin/python3
def uppercase(str):
    upper_str = ''
    for c in str:
        if c >= 'a' and c <= 'z':
            ord_c = ord(c)
            upper_c = ord_c - 32
            upper_str += chr(upper_c)
        else:
            upper_str += c
    print("{}".format(upper_str))
