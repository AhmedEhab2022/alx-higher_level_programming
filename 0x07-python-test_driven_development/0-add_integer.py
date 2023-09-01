#!/usr/bin/python3

def add_integer(a, b=98):
    """Addes two numbers

    Args:
        a: the first number
        b: the second number

    returns the result if success, otherwise raise an exception
    """

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')

    if type(a) == float and a != a:
        raise ValueError('cannot convert a to integer as a is the float NaN')

    if a + 1 == a:
        raise OverflowError('a is too large')

    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    if type(b) == float and b != b:
        raise ValueError('cannot convert b to integer as b is the float NaN')

    if b + 1 == b:
        raise OverflowError('b is too large')

    return (int(a) + int(b))
