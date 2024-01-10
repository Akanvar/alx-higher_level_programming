#!/usr/bin/python3
""" text file-reading function"""

def read_file(filename=""):
        """
    read_file function
    reads a text file (UTF8) and prints it result to stdout
    """
    with open('filename') as f:
        print(f.read(), end="")    
