#!/usr/bin/python3
""" This program print all possible different combinations of numbers 0 - 9

"""
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
