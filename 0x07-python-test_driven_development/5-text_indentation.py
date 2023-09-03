#!/usr/bin/python3
"""Module to print a text with 2 new lines after
each of these characters: ., ?, :
"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text: the text to print

    Return:
        nothing
    """

    if type(text) != str:
        raise TypeError('text must be a string')

    cnt_char1 = 0

    for char in text:
        if char == ' ' and cnt_char1 == 0:
            continue
        print("{}".format(char), end='')
        cnt_char1 += 1
        if char in ['.', '?', ':']:
            print("\n")
            cnt_char1 = 0
