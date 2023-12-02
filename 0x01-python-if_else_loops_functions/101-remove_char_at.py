#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        modified_str = str
    else:
        modified_str = str[:n] + str[(n + 1):]
    return modified_str
