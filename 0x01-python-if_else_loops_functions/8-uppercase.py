#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            character = chr(ord(c) - 32)
        else:
            character = c
        print("{:s}".format(character), end="")
    print('')
