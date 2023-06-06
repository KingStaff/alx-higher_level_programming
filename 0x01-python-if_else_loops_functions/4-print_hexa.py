#!/usr/bin/python3
# 4-print_hexa.py

"""Write a code snippet to print numbers from 0 to 98 in both decimal and hexadecimal formats."""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
