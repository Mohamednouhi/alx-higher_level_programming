#!/usr/bin/python3
"""
This module defines a Base class.
"""

class Base:
    """
    Base class for object management.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The identifier for the instance.

        Attributes:
            id (int): The identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

