#!/usr/bin/python3
for aphla in range(122, 96, -1):
        if aphla % 2 == 0:
                print("{}".format(chr(aphla)), end="")
        else:
                print("{}".format(chr((aphla) - 32)) ,end="")
