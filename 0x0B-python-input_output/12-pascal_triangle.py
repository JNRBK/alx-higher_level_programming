#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    x = ""
    for row in range(1, n):
        x += f"{row}"
    return [x]