#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    ele = 0
    for i in range(list_length):
        try:
            ele = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            ele = 0
            print("division by 0")
        except TypeError:
            ele = 0
            print("wrong type")
        except IndexError:
            ele = 0
            print("out of range")
        finally:
            result.append(ele)

    return result
