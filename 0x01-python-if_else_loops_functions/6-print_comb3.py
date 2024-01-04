#!/usr/bin/python3
for startNumber in range(0, 10):
    for otherNumber in range(startNumner + 1, 10):
        if startNumber == 8 and otherNumber == 9:
            print("{}{}".format(startNumber, otherNumber))
        else:
            print("{}{}, ".format(startNumber, otherNumber), end="")
