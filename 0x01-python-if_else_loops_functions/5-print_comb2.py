#!/usr/bin/python3
for count in range(0, 100):
    if count == 99:
        print("{}".format(count))
    else:
        print("{:02d}, ".format(count), end="")
