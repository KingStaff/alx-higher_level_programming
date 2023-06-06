#!/usr/bin/python3
# 2-print_alphabet.py
"""Write a code snippet to display the lowercase alphabet without including a new line character after each letter."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
