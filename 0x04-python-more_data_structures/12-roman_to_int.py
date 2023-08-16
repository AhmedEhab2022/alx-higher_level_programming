#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        res = 0
        for i in reversed(roman_string):
            if i == 'I':
                if res >= 5:
                    res -= 1
                else:
                    res += 1
            elif i == 'V':
                if res >= 10:
                    res -= 5
                else:
                    res += 5
            elif i == 'X':
                if res >= 50:
                    res -= 50
                else:
                    res += 10
            elif i == 'L':
                if res >= 100:
                    res -= 50
                else:
                    res += 50
            elif i == 'C':
                if res >= 500:
                    res -= 100
                else:
                    res += 100
            elif i == 'D':
                if res >= 1000:
                    res -= 500
                else:
                    res += 500
            elif i == 'M':
                res += 1000
            else:
                return 0
        return res
    else:
        return 0
