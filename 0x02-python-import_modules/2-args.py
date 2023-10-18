#!/usr/bin/python3
import sys

argc = len(sys.argv)
if __name__ == "__main__":
    if argc == 1:
        print(f"{argc - 1} arguments.")
    elif argc == 2:
        print(f"{argc - 1} argument:")
    else:
        print(f"{argc - 1} arguments:")
    index = 1
    while index < argc:
        print(f"{index}: {sys.argv[index]}")
        index += 1
