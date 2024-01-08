#!/usr/bin/python3
""" defines square-printing function """

def print_square(size):
    """ 'print_square' prints a square with the '#' character
     args:
     size: length of the square
     Raises:
         TypeError: if size is not an integer
         ValueError: if size < 0
         TypeError: if size is a float and size < 0
     """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
