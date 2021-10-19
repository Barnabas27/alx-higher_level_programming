#!/usr/bin/python3
"""Class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """comment"""
    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)
        self.size = size
