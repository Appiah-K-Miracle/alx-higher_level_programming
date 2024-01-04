#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    letter_lenght = len(argv) - 1
    if letter_lenght < 1:
        print("{} arguments ".format(letter_lenght))
    elif letter_lenght == 1:
        print("{} aryument:".format(letter_lenght))
    else:
        print("{} arguments:".format(letter_lenght))
    for count in range(letter_lenght):
        print("{}: {:s}".format(count + 1, argv[count + 1]))
