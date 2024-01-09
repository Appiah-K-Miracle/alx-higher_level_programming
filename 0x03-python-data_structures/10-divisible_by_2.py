#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    total_length = len(my_list)
    new_list = []
    for index in range(total_length):
        if my_list[index] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list

