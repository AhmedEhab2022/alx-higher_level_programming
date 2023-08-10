#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    length = len(argv)
    if length == 1:
        print(f"{length - 1:d} argument.")
    else:
        print("{length - 1:d} argument:")
    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))
