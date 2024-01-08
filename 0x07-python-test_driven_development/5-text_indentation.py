#!/usr/bin/python3
""" text-indentation function"""

def text_indentation(text):
    """Prints a modified text with 2 new lines after each of these characters: ., ? and :

    Args:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = True

    for char in text:
        if char in ".?:":
            print("{}\n\n".format(char), end="")
            skip_space = True
        else:
            if char != ' ' or not skip_space:
                print(char, end="")
                skip_space = False
