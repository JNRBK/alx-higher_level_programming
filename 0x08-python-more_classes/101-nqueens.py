#!/usr/bin/python3
import sys
def nqueens(rows, column):
    N = sys.argv[1]
    if sys.argv != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not type(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be a number")
        sys.exit(1)

    return ([rows] * N, [column] * N)