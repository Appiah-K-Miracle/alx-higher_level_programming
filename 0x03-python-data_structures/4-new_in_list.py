#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    letter = my_list[:]
    if idx < 0:
        return letter
    if idx > len(my_list) - 1:
        return letter
    letter[idx] = element
    return letter
