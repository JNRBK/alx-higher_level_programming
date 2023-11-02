#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    v = len(sys.argv) - 1
    if v == 0:
        print("0 arguments.")
    elif v == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(v))

    for i in range(v):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
