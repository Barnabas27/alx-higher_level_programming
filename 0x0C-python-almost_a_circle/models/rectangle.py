#!/usr/bin/python3
"""Class Rectangle"""

import json
from models.base import Base



class Rectangle(Base):
    """comment"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """comment"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """comment"""
        return self.__width

    @width.setter
    def width(self, value):
        """comment"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """comment"""
        return self.__height

    @height.setter
    def height(self, value):
        """comment"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    def area(self):
        """comment"""
        return (self.width * self.height)

    def display(self):
        """comment"""
        string = ""
        for i in range(self.y):
            print()
        for i in range(self.__height):
            string = string + (" " * self.x) + ("#" * self.__width) + "\n"
        print(string[:-1])


    def __str__(self):
        """comment"""
        string = "[Rectangle] (" + str(self.id) + ") "
        string = string + str(self.x) + "/" + str(self.y)
        string = string + " - " + str(self.width) + "/" + str(self.height)
        return string
