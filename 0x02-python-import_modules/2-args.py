#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    number_of_args = len(argv) - 1

    if number_of_args > 1:
        print("{} arguments:".format(number_of_arguments)
        for i in range(1, number_of_args + 1):
            print("{}: {}".format(i, argv[i])
    elif number_of_args == 0:
        print("{} argument.".format(number_of_args))
    else:
        print("{} argument".format(number_of_arguments))
        print("{}. {}".format(number_of_args, argv[1]))
