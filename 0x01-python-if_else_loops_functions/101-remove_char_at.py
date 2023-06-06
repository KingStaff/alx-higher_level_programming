#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(str, n):
    """Create a copy of the string, removing the character at the given C array index position."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
