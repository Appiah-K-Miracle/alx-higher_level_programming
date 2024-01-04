#!/usr/bin/python3
def uppercase(str):
    for generator in str:
        rand = generator
        if ord(rand) >= 97 and ord(rand) <= 122:
            rand = chr(ord(rand) - 32)
        print("{}".format(rand), end="")
    print()
