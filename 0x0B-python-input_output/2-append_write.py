#!/usr/bin/python3
"""Defines append_write module"""


def append_write(filename="", text=""):
    """
    append_write function
    appends a string to the end of a text file (UTF8)
    """

    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
