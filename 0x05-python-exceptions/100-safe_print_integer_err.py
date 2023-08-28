#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    msg = "Exception: Unknown format code 'd' for object of type 'str'"
    try:
        print("{:d}".format(value))
    except Exception as exc:
        print(msg)
        return False

    return True
