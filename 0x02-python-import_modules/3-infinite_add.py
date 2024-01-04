#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    add_num = 0
    for add in range(1, len(argv)):
        add_num = add_num + int(argv[add])
    print("{}".format(add_num))
