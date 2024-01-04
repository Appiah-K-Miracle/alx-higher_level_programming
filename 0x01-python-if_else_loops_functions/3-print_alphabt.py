#!/usr/bin/python3
for alphbet in range(97, 123):
    if alphbet in [101, 113]:
        continue
    print("{}".format(chr(alphbet)), end="")
