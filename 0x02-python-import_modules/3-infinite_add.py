#!/usr/bin/python3
import sys

def args_sum():
    argc = len(sys.argv)
    if argc == 1:
        return 0
    sum = 0
    index = 1
    while index < argc:
        sum += int(sys.argv[index])
        index += 1
    return sum
if __name__ == "__main__":
    print(args_sum())
