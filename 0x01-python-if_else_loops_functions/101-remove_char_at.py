#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str) and n >= 0:
        strcpy = str[0: n] + str[n + 1:]
        return strcpy
    else:
        return str
