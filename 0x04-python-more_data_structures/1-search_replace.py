#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = list(map(lambda line: replace if line == search else line, my_list))
    return my_new_list
