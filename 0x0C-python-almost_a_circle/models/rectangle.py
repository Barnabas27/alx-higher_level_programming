#!/usr/bin/python3
""" Module: rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Instantiation of instance attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
