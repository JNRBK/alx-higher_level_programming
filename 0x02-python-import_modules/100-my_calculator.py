#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    opera = {"+": add, "-": sub, "*": mul, "/": div}
    sign = argv[2]

    if sign not in opera.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a, b = int(argv[1]), int(argv[3])
    print("{:d} {} {:d} = {:d}".format(a, sign, b, opera[sign](a, b)))
