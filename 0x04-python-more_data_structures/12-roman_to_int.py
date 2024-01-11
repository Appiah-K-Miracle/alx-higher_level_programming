#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    my_numbers = [data[x] for x in roman_string] + [0]
    count = 0
    for index in range(len(my_numbers) - 1):
        if my_numbers[index] >= my_numbers[index+1]:
            count += my_numbers[index]
        else:
            count -= my_numbers[index]
    return count
