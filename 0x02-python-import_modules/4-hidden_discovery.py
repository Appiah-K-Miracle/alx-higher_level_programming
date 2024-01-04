#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    entire_names = dir()
    for hide in range(0, len(entire_names)):
        if entire_names[hide][:2] != "_":
            print("{:s}".format(entire_names[hide]))
