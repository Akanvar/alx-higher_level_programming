#!/usr/bin/python3
"""Write file module"""

def write_file(filename="", text=""):
    """
    write_file function
    writes a string to a text file (UTF8)
    """

    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
