#!/usr/bin/python3
def upper_case(c):
    if 96 < ord(c) < 123:
        return (ord(c) - 32)
    else:
        return ord(c)
def uppercase(str):
    new = ""
    for c in str:
        new += "%c" % upper_case(c)
    print("{:s}".format(new))
