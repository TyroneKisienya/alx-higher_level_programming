#!/usr/bin/python3
def print_last_digit(number):
    lst_int = abs(number) % 10
    print("{}".format(lst_int), end="")
    return lst_int
