#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        create_new_string = my_string.translate({ord("c"): None})
        create_new_second_string = create_new_string.translate({ord("C"): None})
        return create_new_second_string
    return my_string
