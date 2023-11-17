#!/usr/bin/python3
"""
This module defines a Square class derived from the Rectangle class.
"""

from rectangle import Rectangle

class Square(Rectangle):
    """Square class for representing squares."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new instance of the Square class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] ({self.id}) {self.get_x()}/{self.get_y()} - {self.get_width()}"

    @property
    def size(self):
        """Gets the size of the square."""
        return self.get_width()

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if value < 0 or not isinstance(value, int):
            raise ValueError(f"Invalid size: {value}")
        self.set_width(value)
        self.set_height(value)

    def update(self, *args, **kwargs):
        """Updates the attributes of the square."""
        if args:
            attrs = ['id', 'size', 'set_x', 'set_y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
            if len(args) > len(attrs):
                raise ValueError("Too many arguments")
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Converts the square to a dictionary."""
        return {"id": self.id, "size": self.size, "x": self.get_x(), "y": self.get_y()}


