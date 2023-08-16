#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = -1e9
        for key in a_dictionary.keys():
            if max_score < a_dictionary[key]:
                max_score = a_dictionary[key]
                max_key = key
        return max_key
    else:
        return None
