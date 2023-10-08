#!/usr/bin/python3
for alpha in range(97, 123):
    if not ((alpha == 113) or (alpha == 101)):
        print("{}".format(chr(alpha)), end="")
