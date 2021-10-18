#!/usr/bin/python3
"""Class Rectangle"""


from models.base import Base
import json


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

    def area(self):
        """comment"""
        return (self.width * self.height)
