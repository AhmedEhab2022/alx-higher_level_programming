#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    result = 0
    size = len(argv)
    for i in range(1, size):
        result += int(argv[i])
    print(f"{result:d}")
