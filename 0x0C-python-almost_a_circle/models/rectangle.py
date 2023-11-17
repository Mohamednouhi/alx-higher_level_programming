#!/usr/bin/python3
"""
This module defines a Rectangle class derived from the Base class.
"""

from base import Base

class Rectangle(Base):
    """Rectangle class for representing rectangles."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of the Rectangle class."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """Gets the width of the rectangle."""
        return self.__width

    def set_width(self, width):
        """Sets the width of the rectangle."""
        if not isinstance(width, int):
            raise TypeError(f"width must be an integer, got {type(width)}")
        if width < 0:
            raise ValueError(f"{width} is not supposed to be negative")
        self.__width = width

    def get_height(self):
        """Gets the height of the rectangle."""
        return self.__height

    def set_height(self, height):
        """Sets the height of the rectangle."""
        if not isinstance(height, int):
            raise TypeError(f"height must be an integer, got {type(height)}")
        if height < 0:
            raise ValueError(f"{height} is not supposed to be negative")
        self.__height = height

    def get_x(self):
        """Gets the x-coordinate of the rectangle."""
        return self.__x

    def set_x(self, x):
        """Sets the x-coordinate of the rectangle."""
        if not isinstance(x, int):
            raise TypeError(f"x must be an integer, got {type(x)}")
        if x < 0:
            raise ValueError(f"{x} is not supposed to be negative")
        self.__x = x

    def get_y(self):
        """Gets the y-coordinate of the rectangle."""
        return self.__y

    def set_y(self, y):
        """Sets the y-coordinate of the rectangle."""
        if not isinstance(y, int):
            raise TypeError(f"y must be an integer, got {type(y)}")
        if y < 0:
            raise ValueError(f"{y} is not supposed to be negative")
        self.__y = y

    def area(self):
        """Computes the area of the rectangle."""
        return self.get_height() * self.get_width()

    def display(self):
        """Displays the rectangle on the console."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle."""
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.__width = args[1]
            if len(args) == 3:
                self.__height = args[2]
            if len(args) == 4:
                self.__x = args[3]
            if len(args) == 5:
                self.__y = args[4]
            if len(args) > 5:
                raise ValueError("Too many arguments")
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.set_width(value)
                if key == 'height':
                    self.set_height(value)
                if key == 'x':
                    self.set_x(value)
                if key == 'y':
                    self.set_y(value)

    def to_dictionary(self):
        """Converts the rectangle to a dictionary."""
        return {"id": self.id, "width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y}

