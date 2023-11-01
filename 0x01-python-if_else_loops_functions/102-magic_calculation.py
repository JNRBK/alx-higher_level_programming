#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a + b == c:
        return (a + b + c) - c
    if a + b > c * 10:
        return (a * b) - c
