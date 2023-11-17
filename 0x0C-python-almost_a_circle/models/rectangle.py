#!/usr/bin/python3
"""Module for Square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class to create and manipulate Square objects."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): Position of square in x.
            y (int): Position of square in y.
            id (int): ID of the new instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size (side length) of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update Square with *args or **kwargs."""
        if args:
            arg_list = list(args)
            if len(arg_list) > 0:
                self.id = arg_list[0]
            if len(arg_list) > 1:
                self.size = arg_list[1]
            if len(arg_list) > 2:
                self.x = arg_list[2]
            if len(arg_list) > 3:
                self.y = arg_list[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        square = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return square

