#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """Convert a string to uppercase and print it."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
